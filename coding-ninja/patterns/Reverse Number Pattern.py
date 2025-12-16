# Problem statement
# Print the following pattern for the given N number of rows.
#
# Pattern for N = 4
# 1
# 21
# 321
# 4321

value = int(input())

for i in range(1, value+1):
    temp = i
    for j in range(1, i+1):
        print(temp, end="")
        temp = temp-1
    print()