import time

import pytest

CUBE_NAME = 'cube-compressed'
ITERATIONS_NUM = 5
ROUNDS_NUM = 5


@pytest.mark.benchmark(
    group="Cube generation with compression",
    timer=time.perf_counter,
    disable_gc=True,
    warmup=False
)
@pytest.mark.usefixtures("remove_generated_cube")
def test_gen_cube_46x10x10(benchmark, cube_util):
    benchmark.pedantic(cube_util.generate_compressed_cube, args=(CUBE_NAME, 46, 10, 10),
                       iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)


@pytest.mark.benchmark(
    group="Cube generation with spatial chunk and compression",
    timer=time.perf_counter,
    disable_gc=True,
    warmup=False
)
@pytest.mark.usefixtures("remove_generated_cube")
def test_gen_cube_46x10x10_spatial_chunk(benchmark, cube_util):
    benchmark.pedantic(cube_util.generate_compressed_cube, args=(CUBE_NAME, 46, 10, 10, (1, 10, 10)),
                       iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)


@pytest.mark.benchmark(
    group="Cube generation with temporal chunk and compression",
    timer=time.perf_counter,
    disable_gc=True,
    warmup=False
)
@pytest.mark.usefixtures("remove_generated_cube")
def test_gen_cube_46x10x10_temporal_chunk(benchmark, cube_util):
    benchmark.pedantic(cube_util.generate_compressed_cube, args=(CUBE_NAME, 46, 10, 10, (46, 1, 1)),
                       iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)


@pytest.mark.benchmark(
    group="Cube generation with compression",
    timer=time.perf_counter,
    disable_gc=True,
    warmup=False
)
@pytest.mark.usefixtures("remove_generated_cube")
def test_gen_cube_46x100x100(benchmark, cube_util):
    benchmark.pedantic(cube_util.generate_compressed_cube, args=(CUBE_NAME, 46, 100, 100), iterations=ITERATIONS_NUM,
                       rounds=ROUNDS_NUM)


@pytest.mark.benchmark(
    group="Cube generation with spatial chunk and compression",
    timer=time.perf_counter,
    disable_gc=True,
    warmup=False
)
@pytest.mark.usefixtures("remove_generated_cube")
def test_gen_cube_46x100x100_spatial_chunk(benchmark, cube_util):
    benchmark.pedantic(cube_util.generate_compressed_cube, args=(CUBE_NAME, 46, 100, 100, (1, 100, 100)),
                       iterations=ITERATIONS_NUM,
                       rounds=ROUNDS_NUM)


@pytest.mark.benchmark(
    group="Cube generation with temporal chunk and compression",
    timer=time.perf_counter,
    disable_gc=True,
    warmup=False
)
@pytest.mark.usefixtures("remove_generated_cube")
def test_gen_cube_46x100x100_temporal_chunk(benchmark, cube_util):
    benchmark.pedantic(cube_util.generate_compressed_cube, args=(CUBE_NAME, 46, 100, 100, (46, 1, 1)),
                       iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)


@pytest.mark.benchmark(
    group="Cube generation with compression",
    timer=time.perf_counter,
    disable_gc=True,
    warmup=False
)
@pytest.mark.usefixtures("remove_generated_cube")
def test_gen_cube_46x720x1440(benchmark, cube_util):
    benchmark.pedantic(cube_util.generate_compressed_cube, args=(CUBE_NAME, 46, 720, 1440), iterations=ITERATIONS_NUM,
                       rounds=ROUNDS_NUM)


@pytest.mark.benchmark(
    group="Cube generation with spatial chunk and compression",
    timer=time.perf_counter,
    disable_gc=True,
    warmup=False
)
@pytest.mark.usefixtures("remove_generated_cube")
def test_gen_cube_46x720x1440_spatial_chunk(benchmark, cube_util):
    benchmark.pedantic(cube_util.generate_compressed_cube, args=(CUBE_NAME, 46, 720, 1440, (1, 720, 1440)),
                       iterations=ITERATIONS_NUM,
                       rounds=ROUNDS_NUM)


@pytest.mark.benchmark(
    group="Cube generation with temporal chunk and compression",
    timer=time.perf_counter,
    disable_gc=True,
    warmup=False
)
@pytest.mark.usefixtures("remove_generated_cube")
@pytest.mark.skip(reason="it takes too long")
def test_gen_cube_46x720x1440_temporal_chunk(benchmark, cube_util):
    benchmark.pedantic(cube_util.generate_compressed_cube, args=(CUBE_NAME, 46, 720, 1440, (46, 1, 1)),
                       iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)
