# Step 1: Take input and write to file
text = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(text + "\n")

print("Data successfully written to output.txt.\n")

# Step 2: Take additional input and append
append_text = input("Enter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(append_text + "\n")

print("Data successfully appended.\n")

# Step 3: Read and display final content
print("Final content of output.txt:\n")

with open("output.txt", "r") as file:
    print(file.read())