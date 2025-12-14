# Problem statement
# Given a number N, print sum of all even numbers from 1 to N.

value = int(input())
sum = 0
while value != 0:
    if value % 2 == 0:
        sum += value
    value-=1

print(sum)