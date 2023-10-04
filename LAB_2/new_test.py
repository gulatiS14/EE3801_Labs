def is_perfect_square(n):
    sqrt_n = int(n**0.5)
    return sqrt_n * sqrt_n == n

def is_fibonacci(n):
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

def steps_to_nearest_fibonacci(x):
    if x <= 0:
        return -1  # Invalid input

    fib1, fib2 = 0, 1
    steps = 0

    while True:
        if is_fibonacci(fib1):
            return steps  - abs(fib1 - x)
        fib1, fib2 = fib2, fib1 + fib2
        steps += 1

x = 15
print(steps_to_nearest_fibonacci(x))  # Output: 2

x = 13
print(steps_to_nearest_fibonacci(x))  # Output: 0