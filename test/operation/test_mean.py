import time

import pytest

from test import config
from test.cube_utils import CubeUtils

ITERATIONS_NUM = getattr(config, 'iterations_num', 1)
ROUNDS_NUM = getattr(config, 'rounds_num', 10)


class TestMean:
    @pytest.fixture(scope="function", autouse=True)
    def ds_135x135(self):
        cube_utils = CubeUtils()
        cube_utils.generate_cube("135x135_chunked_high_res", 46, 2160, 4320, chunksizes=(1, 135, 135))
        ds = cube_utils.open_dataset(cache=True)
        yield ds
        ds.close()

    @pytest.fixture(scope="function", autouse=True)
    def ds_1080x1080(self):
        cube_utils = CubeUtils()
        cube_utils.generate_cube("1080x1080_chunked_high_res", 46, 2160, 4320, chunksizes=(1, 1080, 1080))
        ds = cube_utils.open_dataset(cache=True)
        yield ds
        ds.close()

    @pytest.fixture(scope="function", autouse=True)
    def ds_2160x2160(self):
        cube_utils = CubeUtils()
        cube_utils.generate_cube("2160x2160_chunked_high_res", 46, 2160, 4320, chunksizes=(1, 2160, 2160))
        ds = cube_utils.open_dataset(cache=True)
        yield ds
        ds.close()

    @pytest.fixture(scope="function", autouse=True)
    def ds_46x1080x1080(self):
        cube_utils = CubeUtils()
        cube_utils.generate_cube("46x1080x1080_chunked_high_res", 46, 2160, 4320, chunksizes=(46, 1080, 1080))
        ds = cube_utils.open_dataset(cache=True)
        yield ds
        ds.close()

    # ------------------
    # Spatial-chunk Cube
    # ------------------

    @pytest.mark.benchmark(
        group="All-dimensions mean operation",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=True
    )
    def test_mean_high_res_135x135(self, benchmark, ds_135x135):
        result = benchmark.pedantic(ds_135x135.mean, iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM, warmup_rounds=3)
        assert ('time' not in result)
        assert ('lat' not in result)
        assert ('lon' not in result)
        assert (result['value'].size == 1)

    @pytest.mark.benchmark(
        group="All-dimensions mean operation",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=True
    )
    def test_mean_high_res_1080x1080(self, benchmark, ds_1080x1080):
        result = benchmark.pedantic(ds_1080x1080.mean, iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM, warmup_rounds=3)
        assert ('time' not in result)
        assert ('lat' not in result)
        assert ('lon' not in result)
        assert (result['value'].size == 1)

    @pytest.mark.benchmark(
        group="All-dimensions mean operation",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=True
    )
    def test_mean_high_res_2160x2160(self, benchmark, ds_2160x2160):
        result = benchmark.pedantic(ds_2160x2160.mean, iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM, warmup_rounds=3)
        assert ('time' not in result)
        assert ('lat' not in result)
        assert ('lon' not in result)
        assert (result['value'].size == 1)

    @pytest.mark.benchmark(
        group="LatLon mean operation",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=True
    )
    def test_mean_latlon_high_res_2160x2160(self, benchmark, ds_2160x2160):
        result = benchmark.pedantic(ds_2160x2160.mean, kwargs={'dim': ('lat', 'lon')}, iterations=ITERATIONS_NUM,
                                    rounds=ROUNDS_NUM, warmup_rounds=3)
        assert ('time' in result)
        assert (result['time'].size == 46)
        assert ('lat' not in result)
        assert ('lon' not in result)

    @pytest.mark.benchmark(
        group="LatLon mean operation",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=True
    )
    def test_mean_latlon_high_res_46x1080x1080(self, benchmark, ds_46x1080x1080):
        result = benchmark.pedantic(ds_46x1080x1080.mean, kwargs={'dim': ('lat', 'lon')}, iterations=ITERATIONS_NUM,
                                    rounds=ROUNDS_NUM, warmup_rounds=3)
        assert ('time' in result)
        assert (result['time'].size == 46)
        assert ('lat' not in result)
        assert ('lon' not in result)

    # -------------------
    # Temporal-chunk Cube
    # -------------------

    @pytest.mark.benchmark(
        group="All-dimensions mean operation",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=True
    )
    def test_mean_high_res_46x1080x1080(self, benchmark, ds_46x1080x1080):
        result = benchmark.pedantic(ds_46x1080x1080.mean, iterations=ITERATIONS_NUM, rounds=ROUNDS_NUM, warmup_rounds=3)
        assert ('time' not in result)
        assert ('lat' not in result)
        assert ('lon' not in result)
        assert (result['value'].size == 1)

    @pytest.mark.benchmark(
        group="Temporal mean operation",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=True
    )
    def test_mean_time_high_res_46x1080x1080(self, benchmark, ds_46x1080x1080):
        result = benchmark.pedantic(ds_46x1080x1080.mean, kwargs={'dim': 'time'}, iterations=ITERATIONS_NUM,
                                    rounds=ROUNDS_NUM, warmup_rounds=3)
        assert ('time' not in result)
        assert ('lat' in result)
        assert (result['lat'].size == 2160)
        assert ('lon' in result)
        assert (result['lon'].size == 4320)

    @pytest.mark.benchmark(
        group="Temporal mean operation",
        timer=time.perf_counter,
        disable_gc=True,
        warmup=True
    )
    def test_mean_time_high_res_2160x2160(self, benchmark, ds_2160x2160):
        result = benchmark.pedantic(ds_2160x2160.mean, kwargs={'dim': 'time'}, iterations=ITERATIONS_NUM,
                                    rounds=ROUNDS_NUM, warmup_rounds=3)
        assert ('time' not in result)
        assert ('lat' in result)
        assert (result['lat'].size == 2160)
        assert ('lon' in result)
        assert (result['lon'].size == 4320)
