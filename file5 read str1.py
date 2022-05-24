fobj=open("student.txt","r")
str="_"
while str:
    str=fobj.read()
    print(str)
fobj.close()