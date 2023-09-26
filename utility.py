def approx(a, b, eps = 0.00001):
    return abs(a-b) <= eps

def f(xs: list[float]) -> float:
    return abs(xs[0] - 3.14159265) + abs(xs[1] - 2.71828)

def g(xs: list[float]) -> float:
    return abs(xs[0] - 7.0) + abs(xs[1] - 77.0) + abs(xs[2] - 777.0)

