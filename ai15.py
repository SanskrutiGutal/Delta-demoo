import random
import math

cities = [(0, 0), (2, 3), (5, 2), (6, 6), (8, 3)]

def distance(a, b):
    return math.dist(cities[a], cities[b])

def route_distance(route):
    total = 0
    for i in range(len(route)):
        total += distance(route[i], route[(i + 1) % len(route)])
    return total

def hill_climbing():
    route = list(range(len(cities)))
    random.shuffle(route)

    while True:
        best_route = route
        best_distance = route_distance(route)

        for i in range(1, len(route)):
            for j in range(i + 1, len(route)):
                new_route = route.copy()
                new_route[i], new_route[j] = new_route[j], new_route[i]

                d = route_distance(new_route)

                if d < best_distance:
                    best_distance = d
                    best_route = new_route

        if best_route == route:
            break

        route = best_route

    return route, route_distance(route)

route, total = hill_climbing()

print("Best route:", route + [route[0]])
print("Total distance:", round(total, 2))