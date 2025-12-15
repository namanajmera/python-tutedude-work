
num = int(input())

sum_even = 0
sum_odd = 0

while num > 0:
    rem = num % 10
    if rem %2 == 0:
        sum_even += rem
    else:
        sum_odd += rem
    num = num // 10

print(sum_even, sum_odd)