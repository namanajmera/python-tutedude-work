# x mode is used to create a file.

fh = open("file.txt", "xt")

fh.write("This file is created using the 'x' mode in Python")
fh.write("\nNext Line")

fh.close()
