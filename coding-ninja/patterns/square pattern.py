# Problem statement
# Print the following pattern for the given N number of rows.
#
# Pattern for N = 4
# 4444
# 4444
# 4444
# 4444


value = int(input())
i=0
while i<value:
    j = 0
    while j<value:
        print(value, end='')
        j+=1
    i+=1
    print()