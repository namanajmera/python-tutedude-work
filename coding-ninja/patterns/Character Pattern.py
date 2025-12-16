# Problem statement
# Print the following pattern for the given N number of rows.
#
# Pattern for N = 4
# A
# BC
# CDE
# DEFG


value = int(input())
char = 'A'
char2 = 'A'
for i in range(0,value):
    for j in range(0,i+1):
        print(char, end='')
        char = chr(ord(char)+ 1)
    char2 = chr(ord(char2)+ 1)
    char = char2
    print()