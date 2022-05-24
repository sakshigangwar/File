# file=open("file-question3.txt","w")
# name=[]
# for i in range(5):
#     val=input("enter the name")
#     name.append(val)
# file.writelines(name)   
# print(name)    
# file.close()


banks_list=["kotak","HDFC","SBI","RBL","bank of baroda"]
job=open("str.txt","w")
for i in banks_list:
    value=job.write(i)
    print(i)
job.close()