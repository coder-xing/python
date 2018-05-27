
a=['sd',3,'32',12,'as'] 
for i in range(0,5):
        print('a[{0}]={1}'.format(i,a[i]))
a.remove('sd')
print(a) 

del a[0]
print(a)

a.pop(1)
print(a)
