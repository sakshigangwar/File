file=open("people1.text","r")
count=0
for i in file:
    # i=i.strip("\n")
    count+=1
print(count)
file.close()





