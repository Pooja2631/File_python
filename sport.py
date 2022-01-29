f=open('sport.txt',mode='w+')
i=1
while i<=5:
    name=input("enter any sport name....")
    i=i+1
    data=f.write(name)
    f.write("\n")
    data=f.read()
f.close()
