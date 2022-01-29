f=open('student.txt',mode='r+')
data=f.write("neha->delhi\ndeepti->up\nrani->delhi\naaru->bhiar\nchandni->punjab\npriyanka->shimla\nneela->jaiper\nanisha->delhi\nrachu->bangalor\nhema->mp")
data=f.readlines()
print(len(data))


