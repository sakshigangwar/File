fobj=open("student.txt","r")
str="_"
while str:
    str=fobj.readline()
    print(str)
fobj.close()