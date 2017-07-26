import time

import numpy as np
import pytest
import glob
import os
from netCDF4 import Dataset

LAT_DIM = 10
LON_DIM = 10
TIME_DIM = 46
CHUNK_SIZE = 270
CUBE_NAME = 'cube-default-chunking2'


def generate_cube():
    ds = Dataset(CUBE_NAME + '.nc', 'w', format='NETCDF4_CLASSIC')
    ds.description = 'Sample yearly cube'

    ds.createDimension('time', TIME_DIM)
    ds.createDimension('lat', LAT_DIM)
    ds.createDimension('lon', LON_DIM)

    time_var = ds.createVariable('time', 'f8', 'time')
    lon_var = ds.createVariable('lon', 'f4', 'lon')
    lat_var = ds.createVariable('lat', 'f4', 'lat')
    value = ds.createVariable('value', 'f8', ('time', 'lon', 'lat'))

    lon_range = np.linspace(-180, 180, LON_DIM)
    lon_var[:] = lon_range

    lat_range = np.linspace(-90, 90, LAT_DIM)
    lat_var[:] = lat_range

    time.units = "days since 2015-1-1"
    for i in range(TIME_DIM):
        time_var[i] = i
        value[i, :, :] = np.random.uniform(size=(len(lon_range), len(lat_range)))

    ds.close()


def something(duration=0.0001):
    """
    Function that needs some serious benchmarking.
    """
    time.sleep(duration)
    # You may return anything you want, like the result of a computation
    return 123


@pytest.mark.benchmark(
    group="gen_cube_no_chunking",
    min_time=0.1,
    max_time=5,
    min_rounds=5,
    timer=time.perf_counter,
    disable_gc=True,
    warmup=False
)
def test_gen_cube_no_chunking(benchmark, remove_generated_cube):
    benchmark.pedantic(generate_cube, iterations=5, rounds=10)


@pytest.fixture(scope="session")
def remove_generated_cube():
    yield
    nc_files = glob.glob("*.nc")
    for nc_file in nc_files:
        os.remove(nc_file)
    nc_files = glob.glob("*.nc")
    assert len(nc_files) == 0
