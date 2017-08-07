import glob
import os

import pytest

from .cube_utils import CubeUtils

# -------------------------------------------------------------
# This is a configuration module that is used by py.test.
# py.test will search in this module for any global fixtures.
# -------------------------------------------------------------


@pytest.fixture(scope="function")
def cube_util():
    return CubeUtils()


@pytest.fixture(scope="function")
def remove_generated_cube():
    yield
    cleanup()


@pytest.fixture(scope="class", autouse=False)
def final_cleanup():
    yield
    cleanup()


@pytest.fixture(scope="function", autouse=False)
def final_mem_cleanup():
    yield
    CubeUtils.mem_release()


def cleanup():
    nc_files = glob.glob("*.nc")
    for nc_file in nc_files:
        os.remove(nc_file)
    nc_files = glob.glob("*.nc")
    assert len(nc_files) == 0
