# Lambda Benchmark Functions
These functions are used to get benchmark times of several functions to help identify the optimal method of computation for several simple algorythms

You can test the speed of this function ran on AWS Lambda (unconfigured setup) with running the same funcitons on you GPU or CPU on this [observable notebook](https://observablehq.com/@robsutcliffe/frontend-parallelization-with-gpu-js)


## Matrix Multiplication 
Generates two arrays of number and multiplies each number in each matrix to calculate running a large number of computations  
This is used to benchmark against the example suggested on [The GPU.js documentation](https://github.com/gpujs/gpu.js/#readme)
