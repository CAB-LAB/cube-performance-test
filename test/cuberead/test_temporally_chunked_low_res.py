import time

import pytest

from test.cube_utils import CubeUtils

ITERATIONS_NUM = 5
ROUNDS_NUM = 5


class TestSpatiallyChunkedLowRes:
    # ======================
    # Chunksizes 46 x 1 x 1
    # ======================

    @pytest.fixture(scope="class")
    def cube_46x1x1(self):
        cube_utils = CubeUtils()
        cube_utils.generate_temporal_cube("46x1x1_chunked_low_res", 46, 720, 1440, chunksizes=(46, 1, 1))
        yield cube_utils

    # ---------------
    # Read temporally
    # ---------------

    @pytest.mark.benchmark(
        group="Reading low-res temporal-chunked cube temporally",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_46x1x1_low_res_46x45x45(self, benchmark, cube_46x1x1):
        benchmark.pedantic(cube_46x1x1.read_temporal, args=(45,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading low-res temporal-chunked cube temporally",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_46x1x1_low_res_46x720x720(self, benchmark, cube_46x1x1):
        benchmark.pedantic(cube_46x1x1.read_temporal, args=(720,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    # ---------------
    # Read spatially
    # ---------------

    @pytest.mark.benchmark(
        group="Reading low-res temporal-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_46x1x1_low_res_1x45x45(self, benchmark, cube_46x1x1):
        benchmark.pedantic(cube_46x1x1.read_spatial, args=(45,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading low-res temporal-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_46x1x1_low_res_1x720x720(self, benchmark, cube_46x1x1):
        benchmark.pedantic(cube_46x1x1.read_spatial, args=(720,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

