import random

projects = ["P1", "P2", "P3", "P4", "P5"]
costs = [3, 4, 2, 5, 1]
profits = [5, 7, 4, 9, 2]

budget = 10
POP_SIZE = 30
GENERATIONS = 100

def fitness(chromosome):
    total_cost = sum(c*x for c, x in zip(costs, chromosome))
    total_profit = sum(p*x for p, x in zip(profits, chromosome))

    if total_cost > budget:
        return 0

    return total_profit

def genetic_algorithm():
    population = [
        [random.randint(0, 1) for _ in projects]
        for _ in range(POP_SIZE)
    ]

    for _ in range(GENERATIONS):
        population.sort(key=fitness, reverse=True)
        new_population = population[:2]

        while len(new_population) < POP_SIZE:
            p1, p2 = random.choices(population[:10], k=2)

            point = random.randint(1, len(projects) - 1)
            child = p1[:point] + p2[point:]

            if random.random() < 0.1:
                i = random.randrange(len(projects))
                child[i] = 1 - child[i]

            new_population.append(child)

        population = new_population

    return max(population, key=fitness)

best = genetic_algorithm()

selected = [
    projects[i] for i in range(len(projects)) if best[i] == 1
]

print("Selected projects:", selected)
print("Total cost:", sum(c*x for c, x in zip(costs, best)))
print("Expected profit:", sum(p*x for p, x in zip(profits, best)))