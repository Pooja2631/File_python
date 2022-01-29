# f=open('name.txt',mode='w+')
# data=f.write("deepti")
# f.read()
# print(data)
# f.close()

f=open('name.txt',mode='r+')
data=f.write("deepti->delhi\nchandni->punjab\npriyanka->shimla\nneela->jaiper\nanisha->delhi\nrachu->bangalor\nhema->mp")
data=f.readlines()
print(data)
f.close()

