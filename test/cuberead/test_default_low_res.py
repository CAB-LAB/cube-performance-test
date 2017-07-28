import time

import pytest

from test.cube_utils import CubeUtils

ITERATIONS_NUM = 5
ROUNDS_NUM = 5


class TestDefaultLowRes:
    @pytest.fixture(scope="class", autouse=True)
    def cube_default(self):
        cube_utils = CubeUtils()
        cube_utils.generate_cube("default_low_res", 46, 720, 1440)
        yield cube_utils

    # ---------------
    # Read spatially
    # ---------------

    @pytest.mark.benchmark(
        group="Reading low-res default-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_default_low_res_45x45(self, benchmark, cube_default):
        benchmark.pedantic(cube_default.read_spatial, args=(45,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading low-res default-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_default_low_res_720x720(self, benchmark, cube_default):
        benchmark.pedantic(cube_default.read_spatial, args=(720,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    # ---------------
    # Read temporally
    # ---------------

    @pytest.mark.benchmark(
        group="Reading low-res default-chunked cube temporally",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_default_low_res_46x45x45(self, benchmark, cube_default):
        benchmark.pedantic(cube_default.read_temporal, args=(45,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading low-res default-chunked cube temporally",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_default_low_res_46x1080x1080(self, benchmark, cube_default):
        benchmark.pedantic(cube_default.read_temporal, args=(1080,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)
