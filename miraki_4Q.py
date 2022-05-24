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
