import random
from deap import base, creator, tools

def optimize_schedule(task_list):
    # Create fitness class
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()

    # random permutation of tasks
    toolbox.register("indices", random.sample, range(len(task_list)), len(task_list))
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    # evaluation function
    def eval_order(individual):
        stress_sum = 0
        for i, idx in enumerate(individual):
            stress_sum += task_list[idx]["stress"] * (i + 1)
        return (stress_sum,)

    toolbox.register("evaluate", eval_order)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.2)
    toolbox.register("select", tools.selTournament, tournsize=3)

    # initialize population
    pop = toolbox.population(n=40)

    # evolve
    for _ in range(40):
        offspring = toolbox.select(pop, len(pop))
        offspring = list(map(toolbox.clone, offspring))

        # apply crossover + mutation
        for c1, c2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < 0.5:
                toolbox.mate(c1, c2)
            toolbox.mutate(c1)

        pop[:] = offspring

    return tools.selBest(pop, 1)[0]
