# Problem statement
# Print the following pattern for the given N number of rows.
#
# Pattern for N = 4
# 4444
# 333
# 22
# 1


value = int(input())
val = value
for i in range(0,value):
    for j in range(i,value):
        print(val,end="")
    val-=1
    print()