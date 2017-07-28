import time

import pytest

from test.cube_utils import CubeUtils

ITERATIONS_NUM = 5
ROUNDS_NUM = 5


class TestDefaultLowRes:
    @pytest.fixture(scope="class", autouse=True)
    def cube(self):
        cube_utils = CubeUtils()
        cube_utils.generate_cube("default_low_res", 46, 720, 1440)
        yield cube_utils

    @pytest.mark.benchmark(
        group="Reading default-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_default_low_res_45x45(self, benchmark, cube):
        benchmark.pedantic(cube.read_spatial, args=(45,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading default-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_default_low_res_90x90(self, benchmark, cube):
        benchmark.pedantic(cube.read_spatial, args=(90,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading default-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_default_low_res_180x180(self, benchmark, cube):
        benchmark.pedantic(cube.read_spatial, args=(180,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading default-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_default_low_res_360x360(self, benchmark, cube):
        benchmark.pedantic(cube.read_spatial, args=(360,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading default-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_default_low_res_720x720(self, benchmark, cube):
        benchmark.pedantic(cube.read_spatial, args=(720,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)
