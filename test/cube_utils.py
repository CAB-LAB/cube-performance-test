import os
import sys
import time
import subprocess

import numpy as np
import xarray as xr
import yaml
from netCDF4 import Dataset

CONFIG_FILE = "cube-perf-config.yml"


class CubeUtils:
    def __init__(self):
        self._ds_name = None
        self._time_dim = None
        self._lat_dim = None
        self._lon_dim = None
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as ymlfile:
                config = yaml.load(ymlfile)
            if 'cube_dir' in config:
                self._cube_dir = config['cube_dir']
            else:
                self._cube_dir = None
        else:
            self._cube_dir = None

    def generate_cube(self, cube_name, time_dim, lat_dim, lon_dim,
                      chunksizes=None, compression=False, image_generator=None):

        self._time_dim = time_dim
        self._lat_dim = lat_dim
        self._lon_dim = lon_dim

        if self._cube_dir:
            self._ds_name = os.path.join(self._cube_dir, cube_name + '.nc')
        else:
            self._ds_name = cube_name + '.nc'

        if os.path.exists(self._ds_name):
            return

        ds = Dataset(self._ds_name, 'w', format='NETCDF4_CLASSIC')
        ds.description = 'Sample yearly cube'

        ds.createDimension('time', time_dim)
        ds.createDimension('lat', lat_dim)
        ds.createDimension('lon', lon_dim)

        time_var = ds.createVariable('time', 'f8', 'time')
        lat_var = ds.createVariable('lat', 'f4', 'lat')
        lon_var = ds.createVariable('lon', 'f4', 'lon')
        if chunksizes:
            value = ds.createVariable('value', 'f8', ('time', 'lat', 'lon'), chunksizes=chunksizes, zlib=compression)
        else:
            value = ds.createVariable('value', 'f8', ('time', 'lat', 'lon'), zlib=compression)

        lat_range = np.linspace(-90, 90, lat_dim)
        lat_var[:] = lat_range

        lon_range = np.linspace(-180, 180, lon_dim)
        lon_var[:] = lon_range

        time.units = "days since 2015-1-1"
        for i in range(time_dim):
            time_var[i] = i
            if image_generator:
                value[i, :, :] = image_generator(len(lat_range), len(lon_range))
            else:
                value[i, :, :] = np.random.uniform(size=(len(lat_range), len(lon_range)))
        ds.close()

    def generate_cube_random(self, cube_name, time_dim, lat_dim, lon_dim, chunksizes=None):
        self.generate_cube(cube_name, time_dim, lat_dim, lon_dim, chunksizes=chunksizes)

    def generate_compressed_cube(self, cube_name, time_dim, lat_dim, lon_dim, chunksizes=None):
        self.generate_cube(cube_name, time_dim, lat_dim, lon_dim, chunksizes=chunksizes,
                           image_generator=self.compression_friendly_image_generator, compression=True)

    @staticmethod
    def compression_friendly_image_generator(lat_dim, lon_dim):
        mid_lat = lat_dim // 2
        mid_lon = lon_dim // 2
        array = np.empty((lat_dim, lon_dim))
        array[0:mid_lat, 0:mid_lon] = 0
        array[0:mid_lat, mid_lon: lon_dim] = 1
        array[mid_lat:lat_dim, 0:mid_lon] = 2
        array[mid_lat:lat_dim, mid_lon: lon_dim] = 3
        return array

    def generate_temporal_cube(self, cube_name, time_dim, lat_dim, lon_dim, chunksizes=None):
        self._ds_name = cube_name + '.nc'
        self._time_dim = time_dim
        self._lat_dim = lat_dim
        self._lon_dim = lon_dim

        if self._cube_dir:
            self._ds_name = os.path.join(self._cube_dir, cube_name + '.nc')
        else:
            self._ds_name = cube_name + '.nc'

        if os.path.exists(self._ds_name):
            return

        ds = Dataset(self._ds_name, 'w', format='NETCDF4_CLASSIC')
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

        time_chunk, lat_chunk, lon_chunk = chunksizes
        divisor_lat = self._lat_dim // lat_chunk
        divisor_lon = self._lon_dim // lon_chunk
        lat_pos = 0
        for i in range(divisor_lat):
            lon_pos = 0
            for j in range(divisor_lon):
                value[:, lat_pos:lat_pos + lat_chunk, lon_pos:lon_pos + lon_chunk] = \
                    np.random.uniform(size=(self._time_dim, lat_chunk, lon_chunk))
                lon_pos += lon_chunk
            lat_pos += lat_chunk

        ds.close()

    def read_spatial(self, read_chunk_size):
        ds = xr.open_dataset(self._ds_name, engine='netcdf4', cache=False)
        divisor_lat = self._lat_dim // read_chunk_size
        divisor_lon = self._lon_dim // read_chunk_size
        lat_pos = 0
        data = np.empty((self._lat_dim, self._lon_dim))
        for i in range(divisor_lat):
            lon_pos = 0
            for j in range(divisor_lon):
                data[lat_pos:lat_pos + read_chunk_size, lon_pos:lon_pos + read_chunk_size] = \
                    ds['value'][0, lat_pos:lat_pos + read_chunk_size, lon_pos:lon_pos + read_chunk_size]
                lon_pos += read_chunk_size
            lat_pos += read_chunk_size
        ds.close()
        self.mem_release()
        return data

    def read_spatial_isel(self, read_chunk_size):
        ds = xr.open_dataset(self._ds_name, engine='netcdf4', cache=False)
        divisor_lat = self._lat_dim // read_chunk_size
        divisor_lon = self._lon_dim // read_chunk_size
        lat_pos = 0
        data = np.empty((self._lat_dim, self._lon_dim))
        for i in range(divisor_lat):
            lon_pos = 0
            for j in range(divisor_lon):
                data[lat_pos:lat_pos + read_chunk_size, lon_pos:lon_pos + read_chunk_size] = \
                    ds.isel(lat=slice(lat_pos, lat_pos + read_chunk_size),
                            lon=slice(lon_pos, lon_pos + read_chunk_size))
                lon_pos += read_chunk_size
            lat_pos += read_chunk_size
        ds.close()
        self.mem_release()
        return data

    def read_temporal(self, read_chunk_size):
        ds = xr.open_dataset(self._ds_name, engine='netcdf4', cache=False)
        data = np.empty((self._time_dim, self._lat_dim, self._lon_dim))
        data[0:self._time_dim, 0:read_chunk_size, 0:read_chunk_size] = \
            ds['value'][0:self._time_dim, 0:read_chunk_size, 0:read_chunk_size]
        ds.close()
        self.mem_release()
        return data

    @staticmethod
    def mem_release():
        if sys.platform == 'win32':
            # to clean up standby list in windows, to make sure that each run can always reflect
            # the first run of the command (without any caching)
            subprocess.call(['test\\cuberead\\resources\\EmptyStandbyList.exe', 'standbylist'])
