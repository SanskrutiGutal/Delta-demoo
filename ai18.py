def f(x):
    return -(x - 2) ** 2 + 10

x = 0
step = 0.1

while True:
    current = f(x)

    if f(x + step) > current:
        x += step
    elif f(x - step) > current:
        x -= step
    else:
        break

print("Local maximum position:", round(x, 2))
print("Function value:", round(f(x), 2))