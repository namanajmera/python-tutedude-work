# Problem statement
# Print the following pattern for the given number of rows.
#
# Pattern for N = 5
# E
# DE
# CDE
# BCDE
# ABCDE

value = int(input())
char = chr(ord('A') + value-1)
char2 = chr(ord('A') + value-1)

for i in range(0,value):
    for j in range(0,i+1):
        print(char, end='')
        char = chr(ord(char)+1)
    char2 = chr(ord(char2)-1)
    char = char2
    print()