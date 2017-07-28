import time

import pytest

from test.cube_utils import CubeUtils

ITERATIONS_NUM = 5
ROUNDS_NUM = 5


class TestDefaultHighRes:
    @pytest.fixture(scope="class", autouse=True)
    def cube(self):
        cube_utils = CubeUtils()
        cube_utils.generate_cube("default_low_res", 46, 2160, 4320)
        yield cube_utils

    @pytest.mark.benchmark(
        group="Reading default-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_default_high_res_180x180(self, benchmark, cube):
        benchmark.pedantic(cube.read_spatial, args=(180,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading default-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_default_high_res_360x360(self, benchmark, cube):
        benchmark.pedantic(cube.read_spatial, args=(360,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading default-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_default_high_res_720x720(self, benchmark, cube):
        benchmark.pedantic(cube.read_spatial, args=(720,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading default-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_default_high_res_1080x1080(self, benchmark, cube):
        benchmark.pedantic(cube.read_spatial, args=(1080,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading default-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_default_high_res_2160x2160(self, benchmark, cube):
        benchmark.pedantic(cube.read_spatial, args=(2160,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)
