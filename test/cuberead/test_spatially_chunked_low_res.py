import time

import pytest

from test.cube_utils import CubeUtils

ITERATIONS_NUM = 5
ROUNDS_NUM = 5


class TestSpatiallyChunkedLowRes:
    # ========================
    # Chunksizes 1 x 180 x 180
    # ========================

    @pytest.fixture(scope="class", autouse=True)
    def cube_1x180x180(self):
        cube_utils = CubeUtils()
        cube_utils.generate_cube("default_low_res", 46, 720, 1440, chunksizes=(1, 180, 180))
        yield cube_utils

    @pytest.mark.benchmark(
        group="Cube reading spatial chunking",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x180x180_low_res_45x45(self, benchmark, cube_1x180x180):
        benchmark.pedantic(cube_1x180x180.read_spatial, args=(45,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Cube reading spatial chunking",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x180x180_low_res_90x90(self, benchmark, cube_1x180x180):
        benchmark.pedantic(cube_1x180x180.read_spatial, args=(90,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Cube reading spatial chunking",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x180x180_low_res_180x180(self, benchmark, cube_1x180x180):
        benchmark.pedantic(cube_1x180x180.read_spatial, args=(180,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Cube reading spatial chunking",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x180x180_low_res_360x360(self, benchmark, cube_1x180x180):
        benchmark.pedantic(cube_1x180x180.read_spatial, args=(360,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Cube reading spatial chunking",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x180x180_low_res_720x720(self, benchmark, cube_1x180x180):
        benchmark.pedantic(cube_1x180x180.read_spatial, args=(720,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    # ========================
    # Chunksizes 1 x 90 x 90
    # ========================

    @pytest.fixture(scope="class", autouse=True)
    def cube_1x90x90(self):
        cube_utils = CubeUtils()
        cube_utils.generate_cube("default_low_res", 46, 720, 1440, chunksizes=(1, 90, 90))
        yield cube_utils

    @pytest.mark.benchmark(
        group="Cube reading spatial chunking",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x180x180_low_res_45x45(self, benchmark, cube_1x90x90):
        benchmark.pedantic(cube_1x90x90.read_spatial, args=(45,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Cube reading spatial chunking",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x180x180_low_res_90x90(self, benchmark, cube_1x90x90):
        benchmark.pedantic(cube_1x90x90.read_spatial, args=(90,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Cube reading spatial chunking",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x180x180_low_res_180x180(self, benchmark, cube_1x90x90):
        benchmark.pedantic(cube_1x90x90.read_spatial, args=(180,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Cube reading spatial chunking",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x180x180_low_res_360x360(self, benchmark, cube_1x90x90):
        benchmark.pedantic(cube_1x90x90.read_spatial, args=(360,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Cube reading spatial chunking",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x180x180_low_res_720x720(self, benchmark, cube_1x90x90):
        benchmark.pedantic(cube_1x90x90.read_spatial, args=(720,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)
