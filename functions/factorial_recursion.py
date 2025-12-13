
def factorial(n):
    if n< 0:
        return 0
    if n == 0 | n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(-1))
print(factorial(5))
print(factorial(10))