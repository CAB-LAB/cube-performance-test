import time

import pytest

from test import config
from test.cube_utils import CubeUtils

ITERATIONS_NUM = getattr(config, 'iterations_num', 1)
ROUNDS_NUM = getattr(config, 'rounds_num', 10)


class TestSpatiallyChunkedHighRes:
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
        group="Cube reading for subset spatial analysis high-res",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x135x135_high_res_135x135(self, benchmark, cube_1x135x135):
        benchmark.pedantic(cube_1x135x135.read_spatial, args=(135,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Cube reading for global spatial analysis high-res",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x135x135_high_res_2160x2160(self, benchmark, cube_1x135x135):
        benchmark.pedantic(cube_1x135x135.read_spatial, args=(2160,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    # ---------------
    # Read temporally
    # ---------------

    @pytest.mark.benchmark(
        group="Cube reading for subset temporal analysis high-res",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x135x135_high_res_46x135x135(self, benchmark, cube_1x135x135):
        benchmark.pedantic(cube_1x135x135.read_temporal, args=(135,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Cube reading for global temporal analysis high-res",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x135x135_high_res_46x2160x2160(self, benchmark, cube_1x135x135):
        benchmark.pedantic(cube_1x135x135.read_temporal, args=(2160,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    # ===========================
    # Chunksizes 1 x 1080 x 1080
    # ===========================

    @pytest.fixture(scope="class")
    def cube_1x1080x1080(self):
        cube_utils = CubeUtils()
        cube_utils.generate_cube("1080x1080_chunked_high_res", 46, 2160, 4320, chunksizes=(1, 1080, 1080))
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
    def test_read_1x1080x1080_high_res_135x135(self, benchmark, cube_1x1080x1080):
        benchmark.pedantic(cube_1x1080x1080.read_spatial, args=(135,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Cube reading for global spatial analysis high-res",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x1080x1080_high_res_2160x2160(self, benchmark, cube_1x1080x1080):
        benchmark.pedantic(cube_1x1080x1080.read_spatial, args=(2160,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    # ---------------
    # Read temporally
    # ---------------

    @pytest.mark.benchmark(
        group="Cube reading for subset temporal analysis high-res",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x1080x1080_high_res_46x135x135(self, benchmark, cube_1x1080x1080):
        benchmark.pedantic(cube_1x1080x1080.read_temporal, args=(135,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Cube reading for global temporal analysis high-res",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x1080x1080_high_res_46x2160x2160(self, benchmark, cube_1x1080x1080):
        benchmark.pedantic(cube_1x1080x1080.read_temporal, args=(2160,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    # ==========================
    # Chunksizes 1 x 2160 x 2160
    # ==========================

    @pytest.fixture(scope="class")
    def cube_1x2160x2160(self):
        cube_utils = CubeUtils()
        cube_utils.generate_cube("2160x2160_chunked_high_res", 46, 2160, 4320, chunksizes=(1, 2160, 2160))
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
    def test_read_1x2160x2160_high_res_135x135(self, benchmark, cube_1x2160x2160):
        benchmark.pedantic(cube_1x2160x2160.read_spatial, args=(135,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Cube reading for global spatial analysis high-res",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x2160x2160_high_res_2160x2160(self, benchmark, cube_1x2160x2160):
        benchmark.pedantic(cube_1x2160x2160.read_spatial, args=(1080,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    # ---------------
    # Read temporally
    # ---------------

    @pytest.mark.benchmark(
        group="Cube reading for subset temporal analysis high-res",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x2160x2160_high_res_46x135x135(self, benchmark, cube_1x2160x2160):
        benchmark.pedantic(cube_1x2160x2160.read_temporal, args=(135,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Cube reading for global temporal analysis high-res",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x2160x2160_high_res_46x2160x2160(self, benchmark, cube_1x2160x2160):
        benchmark.pedantic(cube_1x2160x2160.read_temporal, args=(2160,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)
