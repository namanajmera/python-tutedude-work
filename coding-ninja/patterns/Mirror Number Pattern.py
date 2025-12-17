# Problem statement
# Print the following pattern for the given N number of rows.
#
# Pattern for N = 4
#
# Sample
# Input
# 1:
# 3
# Sample
# Output
# 1:\
#   1
#  12
# 123

value = int(input())
for i in range(1, value+1):
    for j in range(1, value-i+1):
        print(end=' ')
    for k in range(1,i+1):
        print(k, end='')
    print()