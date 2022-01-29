def count():
    f=open("mssg.txt",'r')
    d=f.read()
    w=d.split()
    for i in w:
        if i=='My'or i=='Me':
            print(i)
        f.close()
count()