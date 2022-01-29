f=open('yourself.txt',mode='r+')
data=f.write("My first book was Me and My Family. It gave me chance to be Known to the world.")
f.readlines()
i=0
linescount=0
while i<len(data):
    if data[i]=='My' or [i]=='Me':
        linescount=linescount+1
        i=i+1
print(linescount)
f.close()

