


obj1=open("student.txt","w")
for i in range (5):
    name=input("enter the name")
    obj1.write(name)
    obj1.write("\n")
obj1.close()