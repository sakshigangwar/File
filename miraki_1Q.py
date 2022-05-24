# abc=open("people1.text","w")
# for i in range(31):
#     name=input("enter the name:>")
#     abc.write(name)
#     abc.write("\n")
# abc.close()

# a=[4,5,5,5,3,8]
# i=0
# while i<len(a)-2:
#     if a[i]==a[i+2]:
#         print(a[i])
#     i=i+1

city=open("people1.text","r")
for i in city:
    if "delhi" in i:
        city=open("delhi.txt","a")
        city.write(i)
    elif "shimla" in i:
        city=open("shimls.txt","a")
        city.write(i)
    else:
        city=open("other.txt","a")
        city.write(i)
    city.close()