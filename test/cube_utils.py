import os
import time

import numpy as np
import xarray as xr
from netCDF4 import Dataset


class CubeUtils:
    def __init__(self):
        self.ds_name = None
        self.time_dim = None
        self.lat_dim = None
        self.lon_dim = None

    def generate_cube(self, cube_name, time_dim, lat_dim, lon_dim, chunksizes=None):
        self.ds_name = cube_name + '.nc'
        self.time_dim = time_dim
        self.lat_dim = lat_dim
        self.lon_dim = lon_dim

        if os.path.exists(self.ds_name):
            return

        ds = Dataset(self.ds_name, 'w', format='NETCDF4_CLASSIC')
        ds.description = 'Sample yearly cube'

        ds.createDimension('time', time_dim)
        ds.createDimension('lat', lat_dim)
        ds.createDimension('lon', lon_dim)

        time_var = ds.createVariable('time', 'f8', 'time')
        lat_var = ds.createVariable('lat', 'f4', 'lat')
        lon_var = ds.createVariable('lon', 'f4', 'lon')
        if chunksizes:
            value = ds.createVariable('value', 'f8', ('time', 'lat', 'lon'), chunksizes=chunksizes)
        else:
            value = ds.createVariable('value', 'f8', ('time', 'lat', 'lon'))

        lat_range = np.linspace(-90, 90, lat_dim)
        lat_var[:] = lat_range

        lon_range = np.linspace(-180, 180, lon_dim)
        lon_var[:] = lon_range

        time.units = "days since 2015-1-1"
        for i in range(time_dim):
            time_var[i] = i
            value[i, :, :] = np.random.uniform(size=(len(lat_range), len(lon_range)))

        ds.close()

    def read_spatial(self, read_chunk_size):
        ds = xr.open_dataset(self.ds_name, engine='h5netcdf', cache=False)
        divisor_lat = self.lat_dim // read_chunk_size
        divisor_lon = self.lon_dim // read_chunk_size
        lat_pos = 0
        data = np.empty((self.lat_dim, self.lon_dim))
        for i in range(divisor_lat):
            lon_pos = 0
            for j in range(divisor_lon):
                data[lat_pos:lat_pos + read_chunk_size,
                lon_pos:lon_pos + read_chunk_size] = ds['value'][0, lat_pos:lat_pos + read_chunk_size,
                                                     lon_pos:lon_pos + read_chunk_size]
                lon_pos += read_chunk_size
            lat_pos += read_chunk_size
        ds.close()
        return data

    def read_temporal(self, read_chunk_size):
        ds = xr.open_dataset(self.ds_name, engine='h5netcdf', cache=False)
        data = np.empty((self.time_dim, self.lat_dim, self.lon_dim))
        data[0:self.time_dim, 0:read_chunk_size, 0:read_chunk_size] = \
            ds['value'][0:self.time_dim, 0:read_chunk_size, 0:read_chunk_size]
        ds.close()
        return data
