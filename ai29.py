import random

budget = 10
benefits = [8, 5, 6]
costs = [2, 1, 3]

POP_SIZE = 30
GENERATIONS = 100

def fitness(allocation):
    total_cost = sum(c*x for c, x in zip(costs, allocation))
    total_benefit = sum(b*x for b, x in zip(benefits, allocation))

    if total_cost > budget:
        return 0

    return total_benefit

def genetic_algorithm():
    population = [
        [random.randint(0, 5) for _ in benefits]
        for _ in range(POP_SIZE)
    ]

    for _ in range(GENERATIONS):
        population.sort(key=fitness, reverse=True)
        new_population = population[:2]

        while len(new_population) < POP_SIZE:
            p1, p2 = random.choices(population[:10], k=2)

            point = random.randint(1, len(benefits) - 1)
            child = p1[:point] + p2[point:]

            if random.random() < 0.2:
                i = random.randrange(len(benefits))
                child[i] = random.randint(0, 5)

            new_population.append(child)

        population = new_population

    return max(population, key=fitness)

best = genetic_algorithm()

print("Resource allocation:", best)
print("Total cost:", sum(c*x for c, x in zip(costs, best)))
print("Total benefit:", sum(b*x for b, x in zip(benefits, best)))