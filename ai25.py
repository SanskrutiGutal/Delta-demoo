cost = [
    [9, 2, 7],
    [6, 4, 3],
    [5, 8, 1]
]

n = len(cost)
best_cost = float('inf')
best_assignment = []

def solve(worker, used_jobs, total, assignment):
    global best_cost, best_assignment

    if total >= best_cost:
        return

    if worker == n:
        best_cost = total
        best_assignment = assignment.copy()
        return

    for job in range(n):
        if job not in used_jobs:
            solve(
                worker + 1,
                used_jobs | {job},
                total + cost[worker][job],
                assignment + [job]
            )

solve(0, set(), 0, [])

print("Best assignment (job numbers):",
      [job + 1 for job in best_assignment])
print("Minimum cost:", best_cost)