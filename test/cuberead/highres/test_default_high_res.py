import time

import pytest

from test.cube_utils import CubeUtils

ITERATIONS_NUM = 5
ROUNDS_NUM = 5


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
        group="Cube reading for subset spatial analysis high-res",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_default_high_res_135x135(self, benchmark, cube_default):
        benchmark.pedantic(cube_default.read_spatial, args=(135,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Cube reading for global spatial analysis high-res",
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
