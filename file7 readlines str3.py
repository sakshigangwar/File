fobj=open("student.txt","r")
str="_"
size=0
tsize=0
while str:
    str=fobj.readlines()
    size=size+len(str)
    tsize=tsize+len(str.strip())
    print(size)
    print(tsize)


file=open("student.txt","r")
count=0
for i in file:
    count+=1
print(count)