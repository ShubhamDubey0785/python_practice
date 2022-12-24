# f=open("demo.txt","r")  # r for read, and w for writing, and a for append and x for create
# # print(f.read())
# # print(f.readline())
# # print(f.readline())

# f1=open("demo1.txt","w")
# f1.write("this is a file")

# f2=open("demo2.txt","w")
# f2.write("my name is this and \nI am a student of lovelllly professional university")


# for i in f:
#     f1.write(i)

# try:
#     f=open("demo.txt")
#     # your code goes here
# finally:
#     f.close()
# #this way we can make sure that file is closed properly even if exception is raised that cause the program flow to stop


# with open("demo.txt") as f :
#     f.read()
# f=open("demo.txt","r")
# print(f.read(10))
# print(f.tell())


f=open("image.jpg","rb")
print(f.read())

f1=open("image.jpg","wb")

for i in f:
    f1.write(i)

import os
if os.path.exists("demo1.txt"):
    os.remove("demo1.txt")
else:
    print("File does not exist")
    