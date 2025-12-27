
fh = open("file.txt", "rt")

# read() is used to read the content of a file.
# content = fh.read()
'''
# readline() is used to read the content line by line
line1 = fh.readline()
line2 = fh.readline()
line3 = fh.readline()
'''

#  readlines() provide the list of strings which contains content of a file.

lines = fh.readlines()

fh.close()
# print(f"Content of a file: {content}")
'''
print(f"Line 1:- {line1}")
print(f"Line 2:- {line2}")
print(f"Line 3:- {line3}")
'''
print(f"Line 1:- {lines}")
print(type(lines))

for line in lines:
    print(line.rstrip('\n'))