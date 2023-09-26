from collections.abc import Callable


def mutate(par: list, p: int, d: float) -> list:
    newpar = par.copy()
    newpar[p - 1] += d
    return newpar


def hj(f: Callable[[list[float]], float], parv: list[float], maxiter: int, startstep: float, endstep: float) -> list[float]:
    p = len(parv)
    currentstep = startstep
    iter = 0
    par = parv.copy()
    while iter < maxiter:
        fold = f(par)
        fnow = fold
        for currentp in range(1, p + 1):
            mutateleft = mutate(par, currentp, -currentstep)
            fleft = f(mutateleft)
            mutateright = mutate(par, currentp, currentstep)
            fright = f(mutateright)
            if fleft < fold:
                par = mutateleft
                fnow = fleft
            elif fright < fold:
                par = mutateright
                fnow = fright

        if fold <= fnow:
            currentstep = currentstep / 2.0

        if currentstep < endstep:
            break

        iter += 1

    return par
