import time

import pytest

from test.cube_utils import CubeUtils

ITERATIONS_NUM = 5
ROUNDS_NUM = 5


class TestSpatiallyChunkedLowRes:
    # ===========================
    # Chunksizes 1 x 1080 x 1080
    # ===========================

    @pytest.fixture(scope="class", autouse=True)
    def cube_1x1080x1080(self):
        cube_utils = CubeUtils()
        cube_utils.generate_cube("default_low_res", 1, 2160, 4320, chunksizes=(1, 1080, 1080))
        yield cube_utils

    @pytest.mark.benchmark(
        group="Reading spatial-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x1080x1080_low_res_135x135(self, benchmark, cube_1x1080x1080):
        benchmark.pedantic(cube_1x1080x1080.read_spatial, args=(135,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading spatial-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x1080x1080_low_res_270x270(self, benchmark, cube_1x1080x1080):
        benchmark.pedantic(cube_1x1080x1080.read_spatial, args=(270,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading spatial-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x1080x1080_low_res_540x540(self, benchmark, cube_1x1080x1080):
        benchmark.pedantic(cube_1x1080x1080.read_spatial, args=(540,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading spatial-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x1080x1080_low_res_1080x1080(self, benchmark, cube_1x1080x1080):
        benchmark.pedantic(cube_1x1080x1080.read_spatial, args=(1080,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading spatial-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x1080x1080_low_res_2160x2160(self, benchmark, cube_1x1080x1080):
        benchmark.pedantic(cube_1x1080x1080.read_spatial, args=(2160,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    # =========================
    # Chunksizes 1 x 540 x 540
    # =========================

    @pytest.fixture(scope="class", autouse=True)
    def cube_1x540x540(self):
        cube_utils = CubeUtils()
        cube_utils.generate_cube("default_low_res", 1, 2160, 4320, chunksizes=(1, 540, 540))
        yield cube_utils

    @pytest.mark.benchmark(
        group="Reading spatial-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x540x540_low_res_135x135(self, benchmark, cube_1x540x540):
        benchmark.pedantic(cube_1x540x540.read_spatial, args=(135,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading spatial-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x540x540_low_res_270x270(self, benchmark, cube_1x540x540):
        benchmark.pedantic(cube_1x540x540.read_spatial, args=(270,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading spatial-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x540x540_low_res_540x540(self, benchmark, cube_1x540x540):
        benchmark.pedantic(cube_1x540x540.read_spatial, args=(540,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading spatial-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x540x540_low_res_1080x1080(self, benchmark, cube_1x540x540):
        benchmark.pedantic(cube_1x540x540.read_spatial, args=(1080,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading spatial-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x540x540_low_res_2160x2160(self, benchmark, cube_1x540x540):
        benchmark.pedantic(cube_1x540x540.read_spatial, args=(2160,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    # =========================
    # Chunksizes 1 x 270 x 270
    # =========================

    @pytest.fixture(scope="class", autouse=True)
    def cube_1x270x270(self):
        cube_utils = CubeUtils()
        cube_utils.generate_cube("default_low_res", 1, 2160, 4320, chunksizes=(1, 270, 270))
        yield cube_utils

    @pytest.mark.benchmark(
        group="Reading spatial-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x270x270_low_res_135x135(self, benchmark, cube_1x270x270):
        benchmark.pedantic(cube_1x270x270.read_spatial, args=(135,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading spatial-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x270x270_low_res_270x270(self, benchmark, cube_1x270x270):
        benchmark.pedantic(cube_1x270x270.read_spatial, args=(270,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading spatial-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x270x270_low_res_540x540(self, benchmark, cube_1x270x270):
        benchmark.pedantic(cube_1x270x270.read_spatial, args=(540,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading spatial-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x270x270_low_res_1080x1080(self, benchmark, cube_1x270x270):
        benchmark.pedantic(cube_1x270x270.read_spatial, args=(1080,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading spatial-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x270x270_low_res_2160x2160(self, benchmark, cube_1x270x270):
        benchmark.pedantic(cube_1x270x270.read_spatial, args=(2160,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    # =========================
    # Chunksizes 1 x 135 x 135
    # =========================

    @pytest.fixture(scope="class", autouse=True)
    def cube_1x135x135(self):
        cube_utils = CubeUtils()
        cube_utils.generate_cube("default_low_res", 1, 2160, 4320, chunksizes=(1, 135, 135))
        yield cube_utils

    @pytest.mark.benchmark(
        group="Reading spatial-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x135x135_low_res_135x135(self, benchmark, cube_1x135x135):
        benchmark.pedantic(cube_1x135x135.read_spatial, args=(135,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading spatial-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x135x135_low_res_270x270(self, benchmark, cube_1x135x135):
        benchmark.pedantic(cube_1x135x135.read_spatial, args=(270,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading spatial-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x135x135_low_res_540x540(self, benchmark, cube_1x135x135):
        benchmark.pedantic(cube_1x135x135.read_spatial, args=(540,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading spatial-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x135x135_low_res_1080x1080(self, benchmark, cube_1x135x135):
        benchmark.pedantic(cube_1x135x135.read_spatial, args=(1080,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading spatial-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x135x135_low_res_2160x2160(self, benchmark, cube_1x135x135):
        benchmark.pedantic(cube_1x135x135.read_spatial, args=(2160,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)
