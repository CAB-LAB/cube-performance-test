import time

import pytest

CUBE_NAME = 'cube-default-chunking'
ITERATIONS_NUM = 5
ROUNDS_NUM = 5


@pytest.mark.benchmark(
    group="Cube generation with default chunking",
    timer=time.perf_counter,
    disable_gc=True,
    warmup=False
)
@pytest.mark.usefixtures("remove_generated_cube")
def test_gen_cube_46x10x10(benchmark, cube_util):
    benchmark.pedantic(cube_util.generate_cube, args=(CUBE_NAME, 46, 10, 10), iterations=ITERATIONS_NUM,
                       rounds=ROUNDS_NUM)


@pytest.mark.benchmark(
    group="Cube generation with default chunking",
    timer=time.perf_counter,
    disable_gc=True,
    warmup=False
)
@pytest.mark.usefixtures("remove_generated_cube")
def test_gen_cube_46x100x100(benchmark, cube_util):
    benchmark.pedantic(cube_util.generate_cube, args=(CUBE_NAME, 46, 100, 100), iterations=ITERATIONS_NUM,
                       rounds=ROUNDS_NUM)


@pytest.mark.benchmark(
    group="Cube generation with default chunking",
    timer=time.perf_counter,
    disable_gc=True,
    warmup=False
)
@pytest.mark.usefixtures("remove_generated_cube")
def test_gen_cube_46x720x1440(benchmark, cube_util):
    benchmark.pedantic(cube_util.generate_cube, args=(CUBE_NAME, 46, 720, 1440), iterations=ITERATIONS_NUM,
                       rounds=ROUNDS_NUM)
