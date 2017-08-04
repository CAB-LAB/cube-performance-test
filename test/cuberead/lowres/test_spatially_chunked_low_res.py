import time

import pytest

from test import config
from test.cube_utils import CubeUtils

ITERATIONS_NUM = getattr(config, 'iterations_num', 1)
ROUNDS_NUM = getattr(config, 'rounds_num', 10)


class TestSpatiallyChunkedLowRes:
    # =======================
    # Chunksizes 1 x 45 x 45
    # =======================

    @pytest.fixture(scope="class")
    def cube_1x45x45(self):
        cube_utils = CubeUtils()
        cube_utils.generate_cube("45x45_chunked_low_res", 46, 720, 1440, chunksizes=(1, 45, 45))
        yield cube_utils

    # ---------------
    # Read spatially
    # ---------------

    @pytest.mark.benchmark(
        group="Cube reading for small area spatial analysis",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x45x45_low_res_45x45(self, benchmark, cube_1x45x45):
        benchmark.pedantic(cube_1x45x45.read_spatial, args=(45,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Cube reading for large area spatial analysis",
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
        group="Cube reading for subset temporal analysis",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x45x45_low_res_46x45x45(self, benchmark, cube_1x45x45):
        benchmark.pedantic(cube_1x45x45.read_temporal, args=(45,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Cube reading for global temporal analysis",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x45x45_low_res_46x720x720(self, benchmark, cube_1x45x45):
        benchmark.pedantic(cube_1x45x45.read_temporal, args=(720,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

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
        group="Cube reading for small area spatial analysis",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x360x360_low_res_45x45(self, benchmark, cube_1x360x360):
        benchmark.pedantic(cube_1x360x360.read_spatial, args=(45,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Cube reading for large area spatial analysis",
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
        group="Cube reading for subset temporal analysis",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x360x360_low_res_46x45x45(self, benchmark, cube_1x360x360):
        benchmark.pedantic(cube_1x360x360.read_temporal, args=(45,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Cube reading for global temporal analysis",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x360x360_low_res_46x720x720(self, benchmark, cube_1x360x360):
        benchmark.pedantic(cube_1x360x360.read_temporal, args=(720,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    # ========================
    # Chunksizes 1 x 720 x 720
    # ========================

    @pytest.fixture(scope="class")
    def cube_1x720x720(self):
        cube_utils = CubeUtils()
        cube_utils.generate_cube("720x720_chunked_low_res", 46, 720, 1440, chunksizes=(1, 720, 720))
        yield cube_utils

    # ---------------
    # Read spatially
    # ---------------

    @pytest.mark.benchmark(
        group="Cube reading for small area spatial analysis",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x720x720_low_res_45x45(self, benchmark, cube_1x720x720):
        benchmark.pedantic(cube_1x720x720.read_spatial, args=(45,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Cube reading for large area spatial analysis",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x720x720_low_res_720x720(self, benchmark, cube_1x720x720):
        benchmark.pedantic(cube_1x720x720.read_spatial, args=(720,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    # ---------------
    # Read temporally
    # ---------------

    @pytest.mark.benchmark(
        group="Cube reading for subset temporal analysis",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x720x720_low_res_46x45x45(self, benchmark, cube_1x720x720):
        benchmark.pedantic(cube_1x720x720.read_temporal, args=(45,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

    @pytest.mark.benchmark(
        group="Cube reading for global temporal analysis",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=False
    )
    def test_read_1x720x720_low_res_46x720x720(self, benchmark, cube_1x720x720):
        benchmark.pedantic(cube_1x720x720.read_temporal, args=(720,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)

