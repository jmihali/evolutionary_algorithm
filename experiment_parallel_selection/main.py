import random
from deap import base, creator, tools
import numpy as np
import matplotlib.pyplot as plt
import time

# General test configuration
EXPERIMENT_RUNS = 100
GENERATIONS_PER_EXPERIMENT = 20

# Hyperparameters
CROSSOVER_PROBABILITY = 1.0
MUTATION_SIGMA = 0.4
MUTATION_PROBABILITY = 0.9
POPULATION_SIZE_TOURNAMENT = 198
POPULATION_SIZE_RANDOM = 2
TOURNAMENT_SIZE = 4  # TODO(valters) Transform into a percentage of population size.
PLOT_TITLE_EXTENSION = f", Parallel populations ({POPULATION_SIZE_TOURNAMENT} " \
                       f"|| {POPULATION_SIZE_RANDOM})"
VERBOSITY = 0

# Optimization configuration
OBJECTIVE_DIMENSIONS = 5


def alpine2(x: np.array):
    x = np.array(x)
    tmp = np.sqrt(x) * np.sin(x)
    return -np.prod(tmp),


creator.create('FitnessMin', base.Fitness, weights=(-1.0,))
creator.create('Individual', np.ndarray, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register('attr_float', random.uniform, 1, 10)  # Attribute generator
# Structure initializers
toolbox.register('individual', tools.initRepeat, creator.Individual,
                 toolbox.attr_float, OBJECTIVE_DIMENSIONS)
toolbox.register('population', tools.initRepeat, list, toolbox.individual)

toolbox.register('evaluate', alpine2)
toolbox.register('mate', tools.cxTwoPoint)
toolbox.register('mutate', tools.mutGaussian, mu=MUTATION_SIGMA,
                 sigma=MUTATION_PROBABILITY, indpb=0.2)
toolbox.register('select_tournament', tools.selTournament, tournsize=TOURNAMENT_SIZE)
toolbox.register('select_random', tools.selRandom)


def run_evolution(seed, verbosity=0):
    random.seed(seed)
    logbook = tools.Logbook()  # uUsed to store statistics.

    # Create two parallel initial population; individual is a list of integers
    population_tournament = toolbox.population(n=POPULATION_SIZE_TOURNAMENT)
    population_random = toolbox.population(n=POPULATION_SIZE_RANDOM)

    if verbosity > 0:
        print("----- Start of evolution -----")

    # Evaluate both populations
    for population in [population_tournament, population_random]:
        fitness = list(map(toolbox.evaluate, population))
        for individual, individual_fitness in zip(population, fitness):
            individual.fitness.values = individual_fitness
    if verbosity > 0:
        print(f'\t%{len(population_tournament) + len(population_random)} '
              f'individuals evaluated.')

    for generation_index in range(1, GENERATIONS_PER_EXPERIMENT + 1):
        if verbosity > 0:
            print(f"\tGeneration {generation_index}")

        # Tournament selection on all population (parallel population)
        total_population = population_tournament + population_random
        offsprings_tournament = toolbox.select_tournament(total_population,
                                                          len(population_tournament))
        offsprings_tournament = list(map(toolbox.clone, offsprings_tournament))

        # Random selection from population_random (parallel population)
        offsprings_random = toolbox.select_random(population_random,
                                                  len(population_random))
        offsprings_random = list(map(toolbox.clone, offsprings_random))

        for offsprings in [offsprings_tournament, offsprings_random]:
            for individual1, individual2 in zip(offsprings[::2], offsprings[1::2]):
                if random.random() < CROSSOVER_PROBABILITY:
                    toolbox.mate(individual1, individual2)
                    # Old fitness values are no longer valid.
                    del individual1.fitness.values
                    del individual2.fitness.values

            for mutant in offsprings:
                if random.random() < MUTATION_PROBABILITY:
                    toolbox.mutate(mutant)
                    for i, mutant_x in enumerate(mutant):
                        if mutant_x < 0:
                            mutant[i] = 0
                        elif mutant_x > 10:
                            mutant[i] = 10
                    del mutant.fitness.values

            # Evaluate the individuals with an invalid fitness.
            invalid_fitness_individuals = [individual for individual in offsprings
                                           if not individual.fitness.valid]
            fitness = map(toolbox.evaluate, invalid_fitness_individuals)
            for individual, individual_fitness in zip(invalid_fitness_individuals, fitness):
                individual.fitness.values = individual_fitness
            # print(f'\tEvaluated {len(invalid_fitness_individuals)} individuals.')

        population_tournament[:] = offsprings_tournament
        population_random[:] = offsprings_random

        stats = tools.Statistics(key=lambda ind: ind.fitness.values)
        stats.register('size', len)
        stats.register('avg', np.mean)
        stats.register('std', np.std)
        stats.register('min', np.min)
        stats.register('max', np.max)

        total_population = population_tournament + population_random
        record = stats.compile(total_population)
        best_individual = tools.selBest(total_population, 1)[0]
        logbook.record(gen=generation_index, best_ind=best_individual, **record)

        if verbosity > 1:
            print('  Min fit %s' % logbook.select('min')[-1])
            print('  Max fit %s' % logbook.select('max')[-1])
            print('  Avg fit %s' % logbook.select('avg')[-1])
            print('  Std fit %s' % logbook.select('std')[-1])

    best_individual = tools.selBest(total_population, 1)[0]
    if verbosity > 0:
        print('----- End of a (successful) evolution -----')
        print('Best individual is %s, %s' % (best_individual, best_individual.fitness.values))

    return logbook, best_individual


if __name__ == "__main__":
    num_fit120 = 0
    num_fit150 = 0
    num_fit170 = 0
    overall_best_fitness = [0]

    for seed in range(EXPERIMENT_RUNS):
        logbook, best_individual = run_evolution(seed, verbosity=VERBOSITY)
        global_min = -np.power(2.808, OBJECTIVE_DIMENSIONS)

        generation, avg_fitness, experiment_best_fitness = logbook.select('gen', 'avg', 'min')

        if experiment_best_fitness[-1] < -120:
            num_fit120 += 1
        if experiment_best_fitness[-1] < -150:
            num_fit150 += 1
        if experiment_best_fitness[-1] < -170:
            num_fit170 += 1

        if experiment_best_fitness[-1] < overall_best_fitness[-1]:
            overall_best_fitness = experiment_best_fitness
            best_avg_fitness = avg_fitness
            overall_best_individual = best_individual
        print(f"Experiment {seed + 1} . . .\t\t experiments best fitness {experiment_best_fitness[-1]}")

    print('================================================================')

    print('* Experiments with a score better than -120: %d/%d' % (num_fit120, EXPERIMENT_RUNS))
    print('* Experiments with a score better than -150: %d/%d' % (num_fit150, EXPERIMENT_RUNS))
    print('* Experiments with a score better than -170: %d/%d' % (num_fit170, EXPERIMENT_RUNS))

    print('\n\nBest experimental result')
    print('\nBest individual: ', overall_best_individual)
    print('\nBest fitness:', overall_best_fitness[-1])

    # Ploting
    global_min = -np.power(2.808, OBJECTIVE_DIMENSIONS)
    global_min_line = plt.plot([0, generation[-1]], [global_min, global_min], 'g--', label='Global minimum')


    avg_line = plt.plot(generation, best_avg_fitness, 'r--', label='Average fitness')
    best_line = plt.plot(generation, overall_best_fitness, 'b', label='Best fitness')
    global_min_line = plt.plot([0, generation[-1]], [global_min, global_min], 'g--', label='Global minimum')

    plt.xlabel('Generations')
    plt.ylabel('Fitness')
    plt.ylim(global_min - 10, 0)
    plt.title(f'Average and best fitness{PLOT_TITLE_EXTENSION}')
    plt.legend()
    plt.show()




