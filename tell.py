f=open('student.text',mode='r+')
data=f.write("deepti")
data1=f.read(5)
print(data1)
print(f.tell())
f.close()
