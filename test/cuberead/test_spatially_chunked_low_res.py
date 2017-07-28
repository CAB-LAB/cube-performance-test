import time

import pytest

from test.cube_utils import CubeUtils

ITERATIONS_NUM = 5
ROUNDS_NUM = 5


class TestSpatiallyChunkedLowRes:
    # ========================
    # Chunksizes 1 x 360 x 360
    # ========================

    @pytest.fixture(scope="class")
    def cube_1x360x360(self):
        cube_utils = CubeUtils()
        cube_utils.generate_cube("360x360_chunked_low_res", 46, 720, 1440, chunksizes=(1, 360, 360))
        yield cube_utils

    # ---------------
    # Read spatially
    # ---------------

    @pytest.mark.benchmark(
        group="Reading low-res spatial-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x360x360_low_res_45x45(self, benchmark, cube_1x360x360):
        benchmark.pedantic(cube_1x360x360.read_spatial, args=(45,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading low-res spatial-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x360x360_low_res_720x720(self, benchmark, cube_1x360x360):
        benchmark.pedantic(cube_1x360x360.read_spatial, args=(720,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    # ---------------
    # Read temporally
    # ---------------

    @pytest.mark.benchmark(
        group="Reading low-res spatial-chunked cube temporally",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x360x360_low_res_46x45x45(self, benchmark, cube_1x360x360):
        benchmark.pedantic(cube_1x360x360.read_temporal, args=(45,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading low-res spatial-chunked cube temporally",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x360x360_low_res_46x1080x1080(self, benchmark, cube_1x360x360):
        benchmark.pedantic(cube_1x360x360.read_temporal, args=(1080,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    # ========================
    # Chunksizes 1 x 180 x 180
    # ========================

    @pytest.fixture(scope="class")
    def cube_1x180x180(self):
        cube_utils = CubeUtils()
        cube_utils.generate_cube("180x180_chunked_low_res", 46, 720, 1440, chunksizes=(1, 180, 180))
        yield cube_utils

    # ---------------
    # Read spatially
    # ---------------

    @pytest.mark.benchmark(
        group="Reading low-res spatial-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x180x180_low_res_45x45(self, benchmark, cube_1x180x180):
        benchmark.pedantic(cube_1x180x180.read_spatial, args=(45,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading low-res spatial-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x180x180_low_res_720x720(self, benchmark, cube_1x180x180):
        benchmark.pedantic(cube_1x180x180.read_spatial, args=(720,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    # ---------------
    # Read temporally
    # ---------------

    @pytest.mark.benchmark(
        group="Reading low-res spatial-chunked cube temporally",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x180x180_low_res_46x45x45(self, benchmark, cube_1x180x180):
        benchmark.pedantic(cube_1x180x180.read_temporal, args=(45,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading low-res spatial-chunked cube temporally",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x180x180_low_res_46x1080x1080(self, benchmark, cube_1x180x180):
        benchmark.pedantic(cube_1x180x180.read_temporal, args=(1080,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    # ========================
    # Chunksizes 1 x 90 x 90
    # ========================

    @pytest.fixture(scope="class")
    def cube_1x90x90(self):
        cube_utils = CubeUtils()
        cube_utils.generate_cube("90x90_chunked_low_res", 46, 720, 1440, chunksizes=(1, 90, 90))
        yield cube_utils

    # ---------------
    # Read spatially
    # ---------------

    @pytest.mark.benchmark(
        group="Reading low-res spatial-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x90x90_low_res_45x45(self, benchmark, cube_1x90x90):
        benchmark.pedantic(cube_1x90x90.read_spatial, args=(45,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading low-res spatial-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x90x90_low_res_720x720(self, benchmark, cube_1x90x90):
        benchmark.pedantic(cube_1x90x90.read_spatial, args=(720,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    # ---------------
    # Read temporally
    # ---------------

    @pytest.mark.benchmark(
        group="Reading low-res spatial-chunked cube temporally",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x90x90_low_res_46x45x45(self, benchmark, cube_1x90x90):
        benchmark.pedantic(cube_1x90x90.read_temporal, args=(45,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading low-res spatial-chunked cube temporally",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x90x90_low_res_46x1080x1080(self, benchmark, cube_1x90x90):
        benchmark.pedantic(cube_1x90x90.read_temporal, args=(1080,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    # ========================
    # Chunksizes 1 x 45 x 45
    # ========================

    @pytest.fixture(scope="class")
    def cube_1x45x45(self):
        cube_utils = CubeUtils()
        cube_utils.generate_cube("45x45_chunked_low_res", 46, 720, 1440, chunksizes=(1, 45, 45))
        yield cube_utils

    # ---------------
    # Read spatially
    # ---------------

    @pytest.mark.benchmark(
        group="Reading low-res spatial-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x45x45_low_res_45x45(self, benchmark, cube_1x45x45):
        benchmark.pedantic(cube_1x45x45.read_spatial, args=(45,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading low-res spatial-chunked cube spatially",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x45x45_low_res_720x720(self, benchmark, cube_1x45x45):
        benchmark.pedantic(cube_1x45x45.read_spatial, args=(720,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    # ---------------
    # Read temporally
    # ---------------

    @pytest.mark.benchmark(
        group="Reading low-res spatial-chunked cube temporally",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x45x45_low_res_46x45x45(self, benchmark, cube_1x45x45):
        benchmark.pedantic(cube_1x45x45.read_temporal, args=(45,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Reading low-res spatial-chunked cube temporally",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x45x45_low_res_46x1080x1080(self, benchmark, cube_1x45x45):
        benchmark.pedantic(cube_1x45x45.read_temporal, args=(1080,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)
