
try:
    with open("sample.txt", 'wt') as file:
        file.write("This is a sample text file.\n")
        file.write("It contains multiple lines.\n")
except FileNotFoundError:
    print("File not found")

try:
    with open('sample.txt', 'r') as file:
        contents = file.readlines()
    print('Reading file content:')
    index = 1
    for content in contents:
        print(f"Line {index}: {content}", end='')
        index = index + 1
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")