fh = open("file.txt","at")

fh.write('\n')
fh.write("Now the file is open in the a mode.\n")
fh.write("Now instead of override the content, the a mode is use to appending the content in last.\n")

fh.close()

