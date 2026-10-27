import random
import math

cities = [
    (0, 0), (2, 3), (5, 2),
    (6, 6), (8, 3)
]

POP_SIZE = 30
GENERATIONS = 200

def distance(a, b):
    return math.dist(cities[a], cities[b])

def route_distance(route):
    total = 0

    for i in range(len(route)):
        total += distance(
            route[i],
            route[(i + 1) % len(route)]
        )

    return total

def genetic_algorithm():
    n = len(cities)

    population = [
        random.sample(range(n), n)
        for _ in range(POP_SIZE)
    ]

    for _ in range(GENERATIONS):
        population.sort(key=route_distance)
        new_population = population[:2]

        while len(new_population) < POP_SIZE:
            p1, p2 = random.choices(population[:10], k=2)

            point = random.randint(1, n - 1)

            child = p1[:point] + [
                city for city in p2 if city not in p1[:point]
            ]

            if random.random() < 0.2:
                i, j = random.sample(range(n), 2)
                child[i], child[j] = child[j], child[i]

            new_population.append(child)

        population = new_population

    return min(population, key=route_distance)

best = genetic_algorithm()

print("Best route:", best + [best[0]])
print("Total distance:", round(route_distance(best), 2))