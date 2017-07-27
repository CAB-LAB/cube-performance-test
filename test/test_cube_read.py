import time

import pytest

CUBE_NAME = 'cube-default-chunking'
ITERATIONS_NUM = 5
ROUNDS_NUM = 5


@pytest.mark.benchmark(
    group="Cube reading no chunking",
    timer=time.perf_counter,
    disable_gc=True,
    warmup=False
)
@pytest.mark.usefixtures("remove_generated_cube")
def test_read_cube_low_res(benchmark, cube_util):
    cube_util.generate_cube("cube_default_chunking", 46, 720, 1440)
    benchmark.pedantic(cube_util.read_spatial, args=(360,), iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM)
