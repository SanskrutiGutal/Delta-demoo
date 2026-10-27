import random

jobs = [5, 2, 8, 3, 4]
POP_SIZE = 20
GENERATIONS = 100

def fitness(order):
    elapsed = 0
    total = 0

    for job in order:
        elapsed += job
        total += elapsed

    return total

def genetic_algorithm():
    population = [
        random.sample(jobs, len(jobs))
        for _ in range(POP_SIZE)
    ]

    for _ in range(GENERATIONS):
        population.sort(key=fitness)

        new_population = population[:2]

        while len(new_population) < POP_SIZE:
            p1, p2 = random.choices(population[:10], k=2)

            point = random.randint(1, len(jobs) - 1)
            child = p1[:point] + [
                job for job in p2 if job not in p1[:point]
            ]

            if random.random() < 0.2:
                i, j = random.sample(range(len(jobs)), 2)
                child[i], child[j] = child[j], child[i]

            new_population.append(child)

        population = new_population

    return min(population, key=fitness)

best = genetic_algorithm()

print("Best job order:", best)
print("Total completion time:", fitness(best))