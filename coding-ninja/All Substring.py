
str = input()

for i in range(len(str)):
    for j in range(i, len(str)):
        print(str[i:j+1])