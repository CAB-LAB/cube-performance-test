import time

import pytest

from test import config

ITERATIONS_NUM = getattr(config, 'iterations_num', 1)
ROUNDS_NUM = getattr(config, 'rounds_num', 10)


@pytest.mark.benchmark(
    group="Cube generation with compression",
    timer=time.perf_counter,
    disable_gc=True,
    warmup=False
)
@pytest.mark.usefixtures("remove_generated_cube")
def test_gen_cube_46x10x10(benchmark, cube_util):
    benchmark.pedantic(cube_util.generate_compressed_cube, args=('cube-46x10x10-compressed', 46, 10, 10),
                       iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)


@pytest.mark.benchmark(
    group="Cube generation with compression",
    timer=time.perf_counter,
    disable_gc=True,
    warmup=False
)
@pytest.mark.usefixtures("remove_generated_cube")
def test_gen_cube_46x100x100(benchmark, cube_util):
    benchmark.pedantic(cube_util.generate_compressed_cube, args=('cube-46x100x100-compressed', 46, 100, 100),
                       iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)


@pytest.mark.benchmark(
    group="Cube generation with compression",
    timer=time.perf_counter,
    disable_gc=True,
    warmup=False
)
@pytest.mark.usefixtures("remove_generated_cube")
def test_gen_cube_46x720x1440(benchmark, cube_util):
    benchmark.pedantic(cube_util.generate_compressed_cube, args=('cube-46x720x1440-compressed', 46, 720, 1440),
                       iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)
