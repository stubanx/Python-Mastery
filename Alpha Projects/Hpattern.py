def triup(n):
    for i in range(0,n):
        print(" "*(n-i-1),end="")
        print("H"*((2*i)+1),end="")
        print(" "*(n-i-1))
        
def vercal(e,n):
    for i in range(0,6):
        print(" "*e,end="")
        print("H"*n,end="")
        print(" "*2*n,end="")
        print("H"*n,end="")
        print(" "*2*n)
        
def midhoriz(e,n):
    for i in range(0,3):
        print(" "*e,end="")
        print("H"*5*n,end="")
        print(" "*(n-e))

def tridown(n):
    for i in range(0,n):
        print(" "*(3*n+i),end="")
        print("H"*(2*n-2*i-1),end="")
        if i==4:
            break
        print(" "*(1+i))

n=int(input())
triup(n)
e=(2*(n-1)+1-n)//2
vercal(e,n)
midhoriz(e,n)
vercal(e,n)
tridown(n)