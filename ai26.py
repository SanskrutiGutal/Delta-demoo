import random

weights = [2, 3, 4, 5, 9]
values = [3, 4, 5, 8, 10]
capacity = 10

POP_SIZE = 20
GENERATIONS = 100

def fitness(chromosome):
    weight = sum(w * x for w, x in zip(weights, chromosome))
    value = sum(v * x for v, x in zip(values, chromosome))

    if weight > capacity:
        return 0

    return value

def genetic_algorithm():
    population = [
        [random.randint(0, 1) for _ in weights]
        for _ in range(POP_SIZE)
    ]

    for _ in range(GENERATIONS):
        population.sort(key=fitness, reverse=True)

        new_population = population[:2]

        while len(new_population) < POP_SIZE:
            p1, p2 = random.choices(population[:10], k=2)

            point = random.randint(1, len(weights) - 1)

            child = p1[:point] + p2[point:]

            if random.random() < 0.1:
                i = random.randrange(len(weights))
                child[i] = 1 - child[i]

            new_population.append(child)

        population = new_population

    best = max(population, key=fitness)
    return best

best = genetic_algorithm()

print("Selected items:", best)
print("Total weight:", sum(w*x for w, x in zip(weights, best)))
print("Total value:", sum(v*x for v, x in zip(values, best)))