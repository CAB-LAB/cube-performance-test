import time

import pytest

import xarray as xr

from test import config
from test.cube_utils import CubeUtils

ITERATIONS_NUM = getattr(config, 'iterations_num', 1)
ROUNDS_NUM = getattr(config, 'rounds_num', 10)


class TestUfunc:
    @pytest.fixture(scope="function", autouse=True)
    def cube_default_low_res(self):
        cube_utils = CubeUtils()
        cube_utils.generate_cube("default_low_res", 46, 720, 1440)
        yield cube_utils

    @pytest.fixture(scope="function", autouse=True)
    def cube_default_high_res(self):
        cube_utils = CubeUtils()
        cube_utils.generate_cube("default_high_res", 46, 2160, 4320)
        yield cube_utils

    @pytest.mark.benchmark(
        group="Ufunc sqrt operation low-res",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=True
    )
    def test_np_ufunc_default_low_res(self, benchmark, cube_default_low_res):
        result = benchmark.pedantic(cube_default_low_res.np_ufunc_sqrt, iterations=ITERATIONS_NUM, rounds=50,
                                    warmup_rounds=3)
        assert (isinstance(result, xr.core.dataarray.DataArray))
        assert(result.shape == (46, 720, 1440))

    @pytest.mark.benchmark(
        group="Ufunc sqrt operation low-res",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=True
    )
    def test_xr_ufunc_default_low_res(self, benchmark, cube_default_low_res):
        result = benchmark.pedantic(cube_default_low_res.xr_ufunc_sqrt, iterations=ITERATIONS_NUM, rounds=50,
                                    warmup_rounds=3)
        assert (isinstance(result, xr.core.dataarray.DataArray))
        assert (result.shape == (46, 720, 1440))

    @pytest.mark.benchmark(
        group="Ufunc sqrt operation high-res",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=True
    )
    def test_np_ufunc_default_high_res(self, benchmark, cube_default_high_res):
        result = benchmark.pedantic(cube_default_high_res.np_ufunc_sqrt, iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM,
                                    warmup_rounds=3)
        assert (isinstance(result, xr.core.dataarray.DataArray))
        assert (result.shape == (46, 2160, 4320))

    @pytest.mark.benchmark(
        group="Ufunc sqrt operation high-res",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=True
    )
    def test_xr_ufunc_default_high_res(self, benchmark, cube_default_high_res):
        result = benchmark.pedantic(cube_default_high_res.xr_ufunc_sqrt, iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM,
                                    warmup_rounds=3)
        assert (isinstance(result, xr.core.dataarray.DataArray))
        assert (result.shape == (46, 2160, 4320))
