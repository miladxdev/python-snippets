# f(n) -> (n=0 or n=1) ? 1
# f(n) -> (n > 1)      ? f(n-1) + f(n-2)

# fibonacci using reccursion function

def fibonacci(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(4))

# f(4)
# f(3) + f(2)
# f(2) + f(1) + f(1) + f(0)
# f(1) + f(0) + f(1) + f(1) + f(0) => 5


# fibonacci using for loop

def fib(n):
    a = 0
    b = 1
    for i in range(1, n+1):
        c = a + b
        a = b
        b = c
    return b


print(fib(4))
