for i in range(1,6):
    for j in range(1,i+1):
        print('*', end=' ')
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(i, end=' ')
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=' ')
    print()

count = 0
for i in range(1,6):
    for j in range(1,i+1):
        count+=1
        print(count, end=' ')
    print()
