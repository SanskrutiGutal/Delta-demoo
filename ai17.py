import random

jobs = [5, 2, 8, 3, 4]

def total_completion_time(order):
    elapsed = 0
    total = 0

    for job in order:
        elapsed += job
        total += elapsed

    return total

def hill_climbing():
    order = jobs.copy()
    random.shuffle(order)

    while True:
        best = order
        best_cost = total_completion_time(order)

        for i in range(len(order)):
            for j in range(i + 1, len(order)):
                new_order = order.copy()
                new_order[i], new_order[j] = new_order[j], new_order[i]

                cost = total_completion_time(new_order)

                if cost < best_cost:
                    best = new_order
                    best_cost = cost

        if best == order:
            break

        order = best

    return order, total_completion_time(order)

schedule, cost = hill_climbing()

print("Job durations:", schedule)
print("Total completion time:", cost)