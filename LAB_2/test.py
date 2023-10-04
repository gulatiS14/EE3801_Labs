def fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a

def steps_to_nearest_fibonacci(x):
    if x <= 0:
        return -1  # Invalid input

    fib1, fib2 = 0, 1
    steps = 0

    while fib1 < x:
        fib1, fib2 = fib2, fib1 + fib2
        steps += 1

    return min(steps, abs(fib1 - x))

x = 15
print(steps_to_nearest_fibonacci(x))  # Output: 2

x = 13
print(steps_to_nearest_fibonacci(x))  # Output: 0
