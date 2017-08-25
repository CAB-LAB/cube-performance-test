import time

import pytest

from test import config
from test.cube_utils import CubeUtils

ITERATIONS_NUM = getattr(config, 'iterations_num', 1)
ROUNDS_NUM = getattr(config, 'rounds_num', 10)


class TestCorrelation:
    @pytest.fixture(scope="function", autouse=True)
    def cube_multivar(self):
        cube_utils = CubeUtils()
        cube_utils.generate_cube_multivar("135x135_chunked_high_res_2vars", 46, 2160, 4320,
                                          chunksizes=(1, 135, 135), var_num=2)
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
    def test_corr_high_res_135x135(self, benchmark, cube_multivar):
        benchmark.pedantic(cube_multivar.get_corr, iterations=1, rounds=1)

