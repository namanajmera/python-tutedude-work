# Problem statement
# Print the following pattern for the given N number of rows.
#
# Pattern for N = 3
#  A
#  BB
#  CCC

value = int(input())
char = 'A'
for i in range(0,value):
    for j in range(0,i+1):
        print(char,end='')
    char = chr(ord(char)+1)
    print()