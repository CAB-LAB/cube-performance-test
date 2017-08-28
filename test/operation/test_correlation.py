import time

import pytest

from test import config
from test.cube_utils import CubeUtils

ITERATIONS_NUM = getattr(config, 'iterations_num', 1)
ROUNDS_NUM = getattr(config, 'rounds_num', 10)


class TestCorrelation:
    @pytest.fixture(scope="function", autouse=True)
    def cube_multivar_1x135x135(self):
        cube_utils = CubeUtils()
        cube_utils.generate_cube_multivar("135x135_chunked_high_res_2vars", 46, 2160, 4320,
                                          chunksizes=(1, 135, 135), var_num=2)
        yield cube_utils

    @pytest.fixture(scope="function", autouse=True)
    def cube_multivar_46x135x135(self):
        cube_utils = CubeUtils()
        cube_utils.generate_cube_multivar("46x135x135_chunked_high_res_2vars", 46, 2160, 4320,
                                          chunksizes=(46, 135, 135), var_num=2)
        yield cube_utils

    # ------------------
    # Spatial-chunk Cube
    # ------------------

    @pytest.mark.benchmark(
        group="Time dimension correlation operation",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_corr_high_res_135x135(self, benchmark, cube_multivar_1x135x135):
        result = benchmark.pedantic(cube_multivar_1x135x135.get_corr, iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)
        assert ('time' not in result), "'time' dimension should not exist after the correlation operation"
        assert ('lat' in result)
        assert (result['lat'].size == 2160)
        assert ('lon' in result)
        assert (result['lon'].size == 4320)

    # ------------------
    # Temporal-chunk Cube
    # ------------------

    @pytest.mark.benchmark(
        group="Time dimension correlation operation",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_corr_high_res_46x135x135(self, benchmark, cube_multivar_46x135x135):
        result = benchmark.pedantic(cube_multivar_46x135x135.get_corr, iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)
        assert ('time' not in result), "'time' dimension should not exist after the correlation operation"
        assert ('lat' in result)
        assert (result['lat'].size == 2160)
        assert ('lon' in result)
        assert (result['lon'].size == 4320)
