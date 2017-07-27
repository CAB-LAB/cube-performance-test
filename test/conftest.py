import glob
import os

import pytest

from .cube_utils import CubeUtils


@pytest.fixture(scope="function")
def cube_util():
    return CubeUtils()


@pytest.fixture(scope="function")
def remove_generated_cube():
    yield
    cleanup()


def cleanup():
    nc_files = glob.glob("*.nc")
    for nc_file in nc_files:
        os.remove(nc_file)
    nc_files = glob.glob("*.nc")
    assert len(nc_files) == 0


