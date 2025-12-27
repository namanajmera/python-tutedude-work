
# w mode is used to write in a file and if file is already created then it will override the existing file.

fh = open("file.txt", "wt")
fh.write("The File is override using the 'wt' mode in Python")
fh.write('\n w mode is used to write in a file and if file is already created then it will override the existing file.')
fh.write("\n w mode is also used to create a new file if the file is not exists")
fh.close()