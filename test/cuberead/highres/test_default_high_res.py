import time

import pytest

from test import config
from test.cube_utils import CubeUtils

ITERATIONS_NUM = getattr(config, 'iterations_num', 1)
ROUNDS_NUM = getattr(config, 'rounds_num', 10)


class TestDefaultHighRes:
    @pytest.fixture(scope="class", autouse=True)
    def cube_default(self):
        cube_utils = CubeUtils()
        cube_utils.generate_cube("default_high_res", 46, 2160, 4320)
        yield cube_utils

    # ---------------
    # Read spatially
    # ---------------

    @pytest.mark.benchmark(
        group="Cube reading for small area spatial analysis high-res",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_default_high_res_135x135(self, benchmark, cube_default):
        benchmark.pedantic(cube_default.read_spatial, args=(135,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Cube reading for large area spatial analysis high-res",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_default_high_res_2160x2160(self, benchmark, cube_default):
        benchmark.pedantic(cube_default.read_spatial, args=(2160,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    # ---------------
    # Read temporally
    # ---------------

    @pytest.mark.benchmark(
        group="Cube reading for subset temporal analysis high-res",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_default_high_res_46x135x135(self, benchmark, cube_default):
        benchmark.pedantic(cube_default.read_temporal, args=(135,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Cube reading for global temporal analysis high-res",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_default_high_res_46x2160x2160(self, benchmark, cube_default):
        benchmark.pedantic(cube_default.read_temporal, args=(2160,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)
