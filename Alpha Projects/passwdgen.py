import random
a=int(input("How long password should be?: "))
passwd=[]
good=None
while(good!='yes'):
    for i in range(0,a):
        passwd.append(chr(random.randint(0,200)))
    key=''.join(passwd)
    print(key)
    good=input('To confirm the password, enter yes else no:').lower()
with open('passwd.txt','a') as f:
    f.write(key)
print('success')