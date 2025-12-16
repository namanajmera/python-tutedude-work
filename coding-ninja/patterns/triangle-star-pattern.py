# Problem statement
# Print the following pattern for the given N number of rows.
#
# Pattern for N = 4
# *
# **
# ***
# ****
# Note : There are no spaces between the stars (*).

value = int(input())

for i in range(0,value):
    for j in range(0,i+1):
        print("*", end="")
    print()