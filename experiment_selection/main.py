import random
from deap import base, creator, tools
import numpy as np
import matplotlib.pyplot as plt
import time

DIMENSIONS = 5

creator.create('FitnessMin', base.Fitness, weights=(-1.0,))
creator.create('Individual', np.ndarray, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
# Attribute generator
toolbox.register('attr_float', random.uniform, 1, 10)
# Structure initializers
toolbox.register('individual', tools.initRepeat, creator.Individual, toolbox.attr_float, DIMENSIONS)
toolbox.register('population', tools.initRepeat, list, toolbox.individual)

# evaluation function
def alpine2(x):
    # Numpy implementation of alpine2 function. Accepts an array x
    x = np.array(x)
    tmp = np.sqrt(x) * np.sin(x)
    return -np.prod(tmp),


toolbox.register('evaluate', alpine2)
toolbox.register('mate', tools.cxTwoPoint)
toolbox.register('mutate', tools.mutGaussian, mu=0, sigma=0, indpb=0.2)
toolbox.register('select', tools.selRoulette)


# ----------

def run_evolution(seed):
    random.seed(seed)
    logbook = tools.Logbook() # used to store statistics

    # create an initial population of 300 individuals (where
    # each individual is a list of integers)
    pop = toolbox.population(n=200)

    # CXPB  is the probability with which two individuals
    #       are crossed
    #
    # MUTPB is the probability for mutating an individual
    CXPB, MUTPB = 0.6, 0.3

    print('Start of evolution')

    # Evaluate the entire population
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    print('  Evaluated %i individuals' % len(pop))

    # Extracting all the fitnesses of
    # fits = [ind.fitness.values[0] for ind in pop]

    # Variable keeping track of the number of generations
    g = 0

    # Begin the evolution
    while g < 20:
        # A new generation
        g = g + 1
        print('-- Generation %i --' % g)

        # Select the next generation individuals
        offspring = toolbox.select(pop, len(pop))
        # Clone the selected individuals
        offspring = list(map(toolbox.clone, offspring))

        # Apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):

            # cross two individuals with probability CXPB
            if random.random() < CXPB:
                toolbox.mate(child1, child2)

                # fitness values of the children
                # must be recalculated later
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:

            # mutate an individual with probability MUTPB
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        print('  Evaluated %i individuals' % len(invalid_ind))

        # The population is entirely replaced by the offspring
        pop[:] = offspring

        stats = tools.Statistics(key=lambda ind: ind.fitness.values)
        stats.register('size', len)
        stats.register('avg', np.mean)
        stats.register('std', np.std)
        stats.register('min', np.min)
        stats.register('max', np.max)
        record = stats.compile(pop)
        best_ind = tools.selBest(pop, 1)[0]
        logbook.record(gen=g, best_ind = best_ind, **record)

        print('  Min fit %s' % logbook.select('min')[-1])
        print('  Max fit %s' % logbook.select('max')[-1])
        print('  Avg fit %s' % logbook.select('avg')[-1])
        print('  Std fit %s' % logbook.select('std')[-1])

    print('-- End of (successful) evolution --')

    best_ind = tools.selBest(pop, 1)[0]
    print('Best individual is %s, %s' % (best_ind, best_ind.fitness.values))

    return logbook, best_ind


if __name__ == '__main__':
    t_start = time.time()
    logbook, _ = run_evolution(9)
    t_end = time.time()

    global_min = -np.power(2.808, DIMENSIONS) # attention: hard coded

    # load the statistics from the logbook
    gen, avg_fitness, best_fitness = logbook.select('gen', 'avg', 'min')

    print('Total execution time %.6f s' % (t_end-t_start))

    avg_line = plt.plot(gen, avg_fitness, 'r--', label='Average fitness')
    best_line = plt.plot(gen, best_fitness, 'b', label='Best fitness')
    global_min_line = plt.plot([0, gen[-1]], [global_min, global_min], 'g--', label='Global minimum')
    plt.xlabel('Generations')
    plt.ylabel('Fitness')
    plt.ylim(global_min-10, 0)
    plt.title('Average and best fitnesses')
    plt.legend()
    plt.show()