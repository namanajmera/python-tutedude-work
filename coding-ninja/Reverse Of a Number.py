
def reverse(num):
    rev = 0
    temp = num
    while temp > 0:
        rem = temp % 10
        rev = rem + (rev*10)
        temp = temp // 10
    return rev

val = int(input())

print(reverse(val))