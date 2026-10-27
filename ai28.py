import random

# Each class has a faculty and room.
classes = [
    ("F1", "R1"),
    ("F1", "R2"),
    ("F2", "R1"),
    ("F2", "R2")
]

POP_SIZE = 30
GENERATIONS = 100

def fitness(schedule):
    conflicts = 0

    for i in range(len(schedule)):
        for j in range(i + 1, len(schedule)):
            # Classes in the same time slot
            # cannot share a faculty member or room.
            if schedule[i] == schedule[j]:
                continue

            faculty_i, room_i = classes[schedule[i]]
            faculty_j, room_j = classes[schedule[j]]

            if faculty_i == faculty_j:
                conflicts += 1
            if room_i == room_j:
                conflicts += 1

    return conflicts

def genetic_algorithm():
    population = [
        random.sample(range(len(classes)), len(classes))
        for _ in range(POP_SIZE)
    ]

    for _ in range(GENERATIONS):
        population.sort(key=fitness)
        new_population = population[:2]

        while len(new_population) < POP_SIZE:
            p1, p2 = random.choices(population[:10], k=2)

            point = random.randint(1, len(classes) - 1)
            child = p1[:point] + [
                x for x in p2 if x not in p1[:point]
            ]

            if random.random() < 0.2:
                i, j = random.sample(range(len(classes)), 2)
                child[i], child[j] = child[j], child[i]

            new_population.append(child)

        population = new_population

    return min(population, key=fitness)

best = genetic_algorithm()

print("Class order:", best)
print("Conflicts:", fitness(best))