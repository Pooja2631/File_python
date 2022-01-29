f=open('hobby.txt',mode='a+')
i=0
while i<5:
    name=input("enter any hobbies name....")
    i=i+1
    data=f.write(name)
    f.write("\n")
data=f.read()
f.close()

