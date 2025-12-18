# Problem statement
# Write a program that asks the user for a number N and a choice C.
# And then give them the possibility to choose between computing the sum and computing the product of all integers in the range 1 to N (both inclusive).
#
# If C is equal to -
#  1, then print the sum
#  2, then print the product
#  Any other number, then print '-1' (without the quotes)

value = int(input())
choice = int(input())

def sum_of_values(value):
    sum = 0
    for i in range(1,value+1):
        sum+=i
    return sum

def product_of_values(value):
    product = 1
    for i in range(1,value+1):
        product*=i
    return product

if choice == 1:
    print(f"{sum_of_values(value)}")
elif choice == 2:
    print(f"{product_of_values(value)}")
else:
    print(-1)