def fibb(num):
    if num <= 1:
        return num
    else:
        return fibb(num - 1) + fibb(num - 2)

value = int(input())
print(fibb(value))