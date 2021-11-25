from numpy.random import rand
from numpy.random import choice
from numpy.random import randint
from numpy import exp
from numpy import sqrt
from numpy import cos
from numpy import e
from numpy import pi
from numpy import asarray
from numpy import fabs
from numpy import argmin
from numpy import clip
from numpy import any
from numpy import where
from numpy import isclose

# ackley function
def ackley(v):
	x, y = v
	return -20.0 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2))) - exp(0.5 * (cos(2 * pi * x) + cos(2 * pi * y))) + e + 20


def de(fobj, bounds, mut=0.8, crossp=0.7, popsize=20, its=1000):
    dimensions = len(bounds)
    pop = rand(popsize, dimensions)
    min_b, max_b = asarray(bounds).T
    diff = fabs(min_b - max_b)
    pop_denorm = min_b + pop * diff
    fitness = asarray([fobj(ind) for ind in pop_denorm])
    best_idx = argmin(fitness)
    best = pop_denorm[best_idx]
    ended = False
    for i in range(its):
        if(ended == True):
            break
        for j in range(popsize):
            idxs = [idx for idx in range(popsize) if idx != j]
            a, b, c = pop[choice(idxs, 3, replace = False)]
            mutant = clip(a + mut * (b - c), 0, 1)
            cross_points = rand(dimensions) < crossp
            if not any(cross_points):
                cross_points[randint(0, dimensions)] = True
            trial = where(cross_points, mutant, pop[j])
            trial_denorm = min_b + trial * diff
            f = fobj(trial_denorm)
            if f < fitness[j]:
                fitness[j] = f
                pop[j] = trial
                if f < fitness[best_idx]:
                    best_idx = j
                    best = trial_denorm
                    if(f == 0):
                        ended = True
        yield best, fitness[best_idx]



# define range for input
r_min, r_max = -15.0, 15.0
# define the bounds on the search
bounds = [[r_min, r_max], [r_min, r_max]]
# perform the differential evolution search
# print(list(de(ackley, bounds)))
# summarize the result
# print(f'Total Evaluations: {len(result)}')
# evaluate solution
mean_evaluation = 0
for x in range(30):
    result = list(de(ackley, bounds))
    evaluations = len(result)
    mean_evaluation += evaluations
mean_evaluation /= 30
print(mean_evaluation)
# print(f"Solution = {result[-1][0]}")
# evaluation = ackley(solution)
# print('Solution: f(%s) = %.5f' % (solution, evaluation))