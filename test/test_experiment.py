import time
import pytest


def something(duration=0.0001):
    """
    Function that needs some serious benchmarking.
    """
    time.sleep(duration)
    # You may return anything you want, like the result of a computation
    return 123


@pytest.mark.benchmark(
    group="dummy-test",
    min_time=0.1,
    max_time=5,
    min_rounds=5,
    timer=time.perf_counter,
    disable_gc=True,
    warmup=False
)
def test_my_stuff(benchmark):
    # benchmark something
    result = benchmark(something, 2)

    # Extra code, to verify that the run completed correctly.
    # Sometimes you may want to check the result, fast functions
    # are no good if they return incorrect results :-)
    assert result == 123
