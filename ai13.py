def f(x):
    return -(x - 5) ** 2 + 25

x = 0
step = 0.1

while True:
    current = f(x)
    left = f(x - step)
    right = f(x + step)

    if left > current:
        x -= step
    elif right > current:
        x += step
    else:
        break

print("Maximum x:", round(x, 2))
print("Maximum value:", round(f(x), 2))