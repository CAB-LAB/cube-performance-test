# cube-performance-test
A repository to do a performance test on cube generation and access in relation to chunking and compression parameters. The tests are performed using py.test with [benchmark plugin](http://pytest-benchmark.readthedocs.io/en/latest/index.html) which has the ability to display the test results (min, max, mean, std, median, etc.) in a nice table format. These tests will be used to provide a performance guideline in relation to chunking and reading algorithm of the cube data.

## Getting started
The first step is to clone the repository: 

    $ git clone https://github.com/CAB-LAB/cube-performance-test.git
    $ cd cd cube-performance-test
    
### Windows only
To be able to run `EmptyStandbyList.exe` (the tool to wipe file caches), run the test as admin.

### Conda environment
Before starting the test, please create an `esdc` conda environment:

    $ conda env create -f=environment.yml

### Run tests
Sample commands to run the test:
```bash
py.test test                                      # to run all the py.test test plans inside test folder
py.test -sv test                                  # verbose mode
py.test test  --benchmark-sort=mean               # display the results sorted by _mean_ value
py.test test  --benchmark-save=benchmark-report   # save the result in a json file called benchmark-report
```
More py.test benchmark commands can be found [here](http://pytest-benchmark.readthedocs.io/en/latest/index.html).
