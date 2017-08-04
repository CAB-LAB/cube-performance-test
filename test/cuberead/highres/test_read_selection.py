import time

import pytest

from test import config
from test.cube_utils import CubeUtils

ITERATIONS_NUM = getattr(config, 'iterations_num', 1)
ROUNDS_NUM = getattr(config, 'rounds_num', 10)


class TestReadSelection:
    # =========================
    # Chunksizes 1 x 135 x 135
    # =========================

    @pytest.fixture(scope="class")
    def cube_1x135x135(self):
        cube_utils = CubeUtils()
        cube_utils.generate_cube("135x135_chunked_high_res", 46, 2160, 4320, chunksizes=(1, 135, 135))
        yield cube_utils

    # ---------------
    # Read spatially
    # ---------------

    @pytest.mark.benchmark(
        group="Cube subset reading spatially with different selection methods",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_spatial_conventional(self, benchmark, cube_1x135x135):
        benchmark.pedantic(cube_1x135x135.read_spatial, args=(135,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Cube subset reading spatially with different selection methods",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_spatial_isel(self, benchmark, cube_1x135x135):
        benchmark.pedantic(cube_1x135x135.read_spatial_isel, args=(135,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    # ---------------
    # Read temporally
    # ---------------

    @pytest.mark.benchmark(
        group="Cube subset reading temporally with different selection methods",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_temporal_conventional(self, benchmark, cube_1x135x135):
        benchmark.pedantic(cube_1x135x135.read_temporal, args=(135,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Cube subset reading temporally with different selection methods",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_temporal_isel(self, benchmark, cube_1x135x135):
        benchmark.pedantic(cube_1x135x135.read_temporal_isel, args=(135,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)
