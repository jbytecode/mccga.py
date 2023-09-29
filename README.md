# mccga.py
Machine-coded compact genetic algorithm in Python


## In-short

The package implements the Machine-coded compact genetic algorithm defined in 

Satman, M. H. & Akadal, E. (2020). Machine Coded Compact Genetic Algorithms for Real Parameter Optimization Problems . Alphanumeric Journal , 8 (1) , 43-58 . DOI: 10.17093/alphanumeric.576919 [Link](https://dergipark.org.tr/en/pub/alphanumeric/issue/55603/576919)

## Usage 

Suppose the optimization problem is 

$$
\min f(x, y) = \text{abs}(x - 3.14159265) + \text{abs}(y - \exp{1})
$$

then the MCCGA searches for the minimum using 

```python 
def f(xs: list[float]) -> float:
    return abs(xs[0] - 3.14159265) + abs(xs[1] - 2.71828)

rangemin = [-100.0, -100.0]
rangemax = [100.0, 100.0]
mutrate = 0.001
maxiter = 100000
result = optimizer.mccga(f, rangemin, rangemax, mutrate, maxiter)
```


## Other implementations

- Julia (https://github.com/jmejia8/Metaheuristics.jl)
- Rust (https://crates.io/crates/mccga)



## Calling mccga() from R

Thanks to the `reticulate` package, the Python function `mccga()` can be called into R.
Here is the example:

```R
# The package for R & Python integration
library(reticulate)

# Loading the mccga library
source_python("optimizer.py")

# Defining the objective function 
f <- function(xs){
    val <- (xs[1] - 3.14159265)^2 + (xs[2] - 2.71828)^2
    return(val)
}

result <- mccga(f, c(-100, -100), c(100, 100), 0.0001, 100000)

> result
[1] 3.141595 2.718276
```
