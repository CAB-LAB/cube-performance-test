from setuptools import setup
from test.version import __version__

setup(
    name='CubePerformanceTest',
    version=__version__,
    packages=['test'],
    license='MIT',
    long_description=open('README.md').read(),
    requires=['pytest', 'numpy', 'netcdf4']
)