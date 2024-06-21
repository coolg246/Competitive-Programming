# # reading a file using loop

# f = open("file.txt", "r")

# for line in f:
#     print(line)

# f.close()

# # reading a file using read() method

# f = open("file.txt", "r")

# print(f.read())

# f.close()

# reading a file using readline() method

f = open("file.txt", "r")

print(f.readline())

f.close()

# reading a file using readlines() method

f = open("file.txt", "r")

for i in f.readlines():
    print(i)

f.close()

# writing a file using write() method

f = open("file.txt", "w")

f.write("This is a new line")

f.close()

# writing a file using writelines() method

f = open("file.txt", "w")

f.writelines(["This is a new line", "This is another line"])

f.close()

# appending a file using append() method

f = open("file.txt", "a")

f.write("This is a new line")

f.close()

# appending a file using writelines() method

f = open("file.txt", "a")

f.writelines(["This is a new line", "This is another line"])

f.close()

# appending a file using append() method

f = open("file.txt", "a")

f.write("This is a new line")

f.close()

# appending a file using writelines() method

f = open("file.txt", "a")