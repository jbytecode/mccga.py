
from collections.abc import Callable
import random 
import byteworks
import genprobs
import hookejeeves

def isequal(x: float, other: float, mutrate: float) -> bool:
    return abs(x - other) <= mutrate

def isconverged(probvector: list[float], mutrate: float) -> bool:
    n = len(probvector)
    satisfied = 0
    for i in range(n):
        val = probvector[i];
        if isequal(val, 0.0, mutrate) or isequal(val, 1.0, mutrate):
            satisfied += 1
        else:
            break

    return satisfied == n;


def binarycost(fcost: Callable[[list[float]], float], candidate: list[int]) -> float:
    doubles = byteworks.bits_to_floats(candidate)
    result = fcost(doubles);
    return result


def sample(probvector: list[float]) -> list[int]:
    n = len(probvector)
    newvector = [0] * n
    
    for i in range(n):
        if random.random() < probvector[i]:
            newvector[i] = 1
    
    return newvector


def update(probvector: list[float], winner: list[int], loser: list[int], mutrate: float):
    for i in range(len(probvector)):
        if winner[i] != loser[i]:
            if winner[i] == 0:
                probvector[i] = max(probvector[i] - mutrate, 0.0)
            else:
                probvector[i] = min(probvector[i] + mutrate, 1.0)
            


def mccga_singleiter(probvect: list[float], fcost: Callable[[list[float]], float], mutrate: float):
    candidate1 = sample(probvect)
    candidate2 = sample(probvect)
    cost1 = binarycost(fcost, candidate1)
    cost2 = binarycost(fcost, candidate2)
    winner = candidate1
    loser = candidate2
    if cost2 < cost1:
        winner = candidate2
        loser = candidate1
    
    update(probvect, winner, loser, mutrate)



def mccga(
    fcost: Callable[[list[float]], float],
    mins: list[float],
    maxs: list[float],
    mutrate: float,
    maxiter: int,
) -> list[float]:
    
    probvect = genprobs.generate_probability_vector(mins, maxs, 500000)

    iter = 0;

    while iter < maxiter:
        mccga_singleiter(probvect, fcost, mutrate)
        if isconverged(probvect, mutrate):
            break
        iter = iter + 1

    firstresult =  byteworks.bits_to_floats(sample(probvect))
    
    secondresult = hookejeeves.hj(fcost, firstresult, 1000, 5.0, 0.00001)
    
    return secondresult