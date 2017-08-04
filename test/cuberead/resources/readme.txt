EmptyStandbyList.exe is a command line wrapper of RamMap (https://docs.microsoft.com/en-us/sysinternals/downloads/rammap),
a tool to manage the memory usage in Windows. This tool is very important in this project because when reading netcdf file
using xarray (or even without? need more information), it is straight away stored in memory. When the dataset is then
deleted or de-referenced, this file still exists in the memory in the Standby List. It is there, it will be used if it is
called again in the future, but if more memory is needed for any other processes, the memory section occupied by this
entry will be overwritten. However, for this performance test, it is desirable to simulate a 'first-time' case for each
test run, which means without caching. This is where EmptyStandbyList.exe comes into play. After each reading of netcdf
file, this command is executed, to ensure a non-cached reading on the next test round.

The executable is available here: https://wj32.org/wp/software/empty-standby-list/