f=open(input('Enter file: '),'r')
c=[]
for x in f:
    c+=x.split(' ')
print(len(c))