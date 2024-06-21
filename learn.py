# copy a file source to destination without duplicate

f = open("Socket Programming/file1.txt", "r+")

f1 = open("Socket Programming/file2.txt", "w+")

print(f.readlines())
print(f1.readlines())

for i in f.readlines():
    print(i)
    if i not in f1.readlines():
        f1.write(i)

f.close()
