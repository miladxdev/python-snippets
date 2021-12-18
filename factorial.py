# find the factorial of a number
# n! = n * (n-1) * (n-2) * ...

# 1.using recurssion function
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


print(factorial(4))

# factorial(4)                => 24
# 4 * factorial(3)           = 24
#     3 * factorial(2)      = 6
#         2 * factorial(1) = 2
#             => 1


# 2.factorial using a for loop
def fact(x):
    result = 1
    for i in range(1, x):
        result = result * (i + 1)

    return result


print(fact(4))
