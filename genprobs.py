import random
import byteworks

def random_vector_between(mins: list, maxs: list) -> list:
    n = len(mins)
    result = [0.0] * n

    for i in range(n):
        result[i] = mins[i] + random.random() * (maxs[i] - mins[i])
    
    return result


def generate_probability_vector(mins: list, maxs: list, ntries: int) -> list:
    nbits = len(mins) * 32
    mutrate = 1.0 / ntries
    probvector = [0.0] * nbits
    
    for _ in range(ntries):
        floats = random_vector_between(mins, maxs)
        floatbits = byteworks.floats2bits(floats)
        for k in range(nbits):
            if floatbits[k] == 1:
                probvector[k] = probvector[k] + mutrate

    return probvector