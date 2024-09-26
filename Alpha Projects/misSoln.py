# simple interest
# p=int(input())
# a= p*int(input())*int(input())//100
# print(p+a)


# compound interest
# p=int(input())
# r=int(input())
# tw=int(input())
# t=0
# for i in range(tw):
#     interest=p*r/100
#     p+=interest
#     t+=interest
# print(t)


# wonderful chocoate offer
# n=list(map(int,input().split()))
# c= int(n[0])
# l= int(n[1])
# d= int(n[2])
# print(c+((d-1)*l))


# ant consensus
# a=list(map(int,input().split()))
# c=int(a[0])
# k=int(a[1])
# n=int(a[2])

# for i in range(n):
#     tp=c*k
#     c=tp
# print(c)


# encoded Name
# n= list(map(int,input().split("&")))
# a=[]
# for i in n:
#     a.append(chr(i))
# f="".join(a)
# print(f)


    


# n=int(input("enter"))
# s=n
# sum=0
# while n>0:
#     ld=s%10
#     sum= sum*10 +ld
#     s//=10
# if sum==n:
#     print("yes")
# else:
#     print("no")


# n=int(input())
# sum=0
# ld=0
# while n>0:
#     ld=n%10
#     n//10
#     sum+=ld
# print(sum)

# raj=input()
# lia=raj.split(" ")
# lias=[]
# for i in lia:
#     lias.append(int(i))
# print(sum(lias))


# n=int(input())
# s=n
# sum=0
# while n>0:
#     ld=n%10
#     n//=10
#     sum=sum*10 +ld
# print("yes" if sum==s else "no")


# sum of lists
# a=input()
# list_a=a.split(" ")
# alist=[]
# for i in list_a:
#     alist.append(int(i))
# print(sum(alist))


# copy the array
# a=input()
# b=int(input())
# lis=a.split(" ")
# lisnum=[]
# for i in lis:
#     f=int(i)+ b
#     lisnum.append(str(f))
# x=",".join(lisnum)
# print(x)


# max min of array
# a=input()
# lis=a.split(" ")
# lisnum=[]
# for i in lis:
#     lisnum.append(i)
# set(lisnum)
# print(lisnum[0],lisnum[-1])


# search element
# n=[]

# for i in range(0,4):
#     i=int(input())
#     n.append(i)
    
# b=int(input())
    
# for i in range(0,4):
#     if n[i]==b:
#         True
#     else: False


# od-even
# a=input()
# lis=a.split(" ")
# lisnum=[]
# for i in lis:
#     lisnum.append(int(i))
# print(lisnum)
# e=[]
# o=[]
# coune=0
# couno=0

# for j in lisnum:
#     if j%2==0:
#         e.append(j)
#         coune+=1
#     else:
#         o.append(j)
#         couno+=1

# print(f"even{coune}{len(e)}{" ".join(str(e))}\nodd{couno}{len(o)}{" ".join(str(o))}")


# A = [3, 5, 1, 2, 1, 2]
# n=[]
# i=0

# for i in range(len(A)-1,-1,-1):
#     n.append(A[i])
# print(n)
# A.reverse()
# print(A)


# add of two strings
# a=[1, 2, 3,4]
# b=[4, 5, 6,7]
# x=[]
# for i in range(0,len(a),1):
#     x.append(a[i]+b[i])
# print(x)


# list = [2,4,6,8,10,12,14,16,18,20]

# print(list[:])    #all
# print(list[::])     #all
# print(list[2:5])  #6,8,10
# print(list[2:])    #6 to al
# print(list[2::])    #6 to all
# print(list[:2])    #2,4
# print(list[::2])   #2,6,10,14,18
# print(list[1::2])     #4,8,12,16,20
# print(list[2:10:2])  #6,10,14,18
# list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
# print(len(list))
# print(list[-2 :-5: -1])  

# t = "2 3 4 5 6"
# print(t.split())    

# l1 = [1, 2, 3, 5, 8, 9]           
# l2 = [3, 4, 5 , 6, 7, 10]
# result = l1 + l2
# print(result)

# result1 = l1 * 3
# print(result1)





# a=input()
# vowels='aeiouAEIOU'
# counv=0
# counc=0
# for char in a:
#     if char in vowels:
#         counv+=1
#     else:
#         counc+=1
# print(counv,counc)


# a=input()
# print(len(a))
# a=input()
# ele=[]
# c=''
# for i in a:
#     ele.append(i)
# ele.reverse()
# for j in ele:
#     c+=j
# print("1" if a==c else "0")


# reverse of string
# a=input()
# b=a[::-1]
# print("1" if a==b else "0")
# reverse of int
# a=int(input())
# a=str(a)
# b=(a[::-1])
# int(a)
# int(b)
# print("1" if a==b else "0")


# a=input()
# start=0
# end=1
# for i in range(0,len(a)):
#     if a[i]=='*':
#         start+=1
#     elif a[len(a)-i]=='*':
#         end+=1
#     else:
#         break
# print(a[start:(len(a)-end)])




# a=input()
# start=0
# for i in a:
#     if i=='*':
#         start+=1
#     else:
#         break
# print(a[start:])
    
    
    
# a=input()
# end=0
# for i in range(1,len(a)):
#     if a[len(a)-i]=='*':
#         end+=1
#     else:
#         break
# print(a[:len(a)-end])

# reverse string
# a=input()
# print(a[::-1])


# reverse order of words
# a=input()
# n=a.split(" ")
# n.reverse()
# print(" ".join(n))



# reverse
# a=input()
# n=a.split()
# new=[]
# for i in range(len(n)):
#     new.append(n[i][::-1])
# print(" ".join(new))


# wordplay()
# a=input()
# print(a.lower())
# print(a.upper())
# print(a.capitalise())
# print(a.title())


# first occurance
# a=input()
# b=int(input())
# coun1=0
# chr(b)
# for i in a:
#     if i==chr(b):
#         coun1+=1
# print(coun1)


# # word occurance
# string=input()
# word=input()
# count=0
# for i in range(len(string)-1):
#     if string[i]+string[i+1]==word:
#         count+=1
# print(count)
    
    
    
# word occurance
# string=input()
# word=input()
# count=0
# for i in range(len(string)-1):
#     a=string[i]+string[i+1]
#     if a==word and a.islower():
#         count+=1
# print(count)



# string operations
# a=input()
# g=''
# vowels='a','e','i','o','u'
# for i in a:
#     if i.islower():
#         if i in 'aeiou':
#             i='#'
#         g=g+i
# print(g*2)

# a=int(input())
# while a>0:
#     print(a,end=' ')
#     a-=1
    
# for i in range(5,0,-1):
#     print(i,end=" ")


# a=input()
# lis=a.split(" ")
# lis.reverse()
# print(" ".join(lis))
# 
# 
# 
# 
# 
# 
# Which of the following data types in Python is mutable? 
# A) Tuple
# B) List
# C) String
# D) Set
# Answer: B) List
# What is the output of the following code?

# s = {2, 3, 4, 5} 
# s.add(2) 
# print(len(s)) 

# A) 4
# B) 5
# C) 3
# D) 2
# Answer: A) 4

# Which method can be used to remove an item from a set if it is present in the set? 
# A) discard()
# B) remove()
# C) pop()
# D) delete()
# Answer: B) remove()

# What will be the output of the following code?
# d = {"one": 1, "two": 2, "three": 3} 
# del d["two"] 
# print(len(d)) 
# A) 3
# B) 1
# C) 2
# D) Error
# Answer: A) 3
# Which of the following is not a valid way to create a dictionary in Python? 
# A) d = {}
# B) d = dict()
# C) d = {"one": 1, "two": 2}
# D) d = {("one", 1), ("two", 2)}
# Answer: D) d = {("one", 1), ("two", 2)}

# What will be the output of the following code?
# x = 10 y = 12 
# if x > y: print("x is greater") 
# elif x < y: print("y is greater") 
# else: print("Both are equal") 
# A) x is greater
# B) y is greater
# C) Both are equal
# D) No output
# Answer: B) y is greater
# In Python, how can you convert a string to uppercase? 
# A) str.upper()
# B) str.to_upper()
# C) str.casefold()
# D) str.capital()
# Answer: A) str.upper()
# What will be the output of the following code?
# s = "Python" print(s[1:4]) 
# A) Py
# B) yth
# C) ytho
# D) yth
# Answer: B) yth
# Which of the following is the correct way to check if a key exists in a dictionary d in Python? A) key in d
# B) d.has_key(key)
# C) d.contains(key)
# D) key.exists(d)
# Answer: A) key in d
# What does the set() function do in Python? A) Converts a list into a set
# B) Converts a set into a list
# C) Concatenates two sets
# D) Splits a set into multiple sets
# Answer: A) Converts a list into a set

# Which of the following is the correct way to iterate over a dictionary d in Python? 
# A) for key, value in d:
# B) for key in d.keys():
# C) for key, value in d.items():
# D) for value in d.values():
# Answer: C) for key, value in d.items():

# What will be the output of the following code?
# x = 5 result = "Even" if x % 2 == 0 else "Odd" print(result) 
# A) Even
# B) Odd
# C) 1
# D) Error
# Answer: B) Odd


# a=input()
# print(a,end=" ")


# adi=a.split()
# print(adi,end=" ")

# adi.reverse()
# print(adi)

# print(" ".join(adi))



# input=[[1,2,3],[4,5,6],[7,8,9]]
# a=0
# for i in input:
#     i.sort()
#     a+= i[len(i)-1]
# print(l)



# "(())"
# "))(())"
# "()()()"
# "()())"
# "()))"


# input="(())("
# openp=0
# closp=0
# result=True
# for i in input:
#     if i==')':
#         closp+=1
#     if i=='(':
#         openp+=1
#     if openp<closp:
#         result= False
#         break    
# if openp!=closp:
#     result=False
# print(result)   
    
    
    
    
    # fibonacci
# num=int(input())
# a=0
# lnum=1
# for i in range(2,9+1):
#     g=a+lnum
#     a=lnum
#     lnum=g
# print(g)
    
    
#  no palindrome
# a= int(input())
# a=str(a)
# b= a[::-1]
# if a==b:
#     print(True)
# else:
#     print(False)


# perfect no.

# n=int(input())
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print(True)
# else:
#     print(False)
    
    
# strong no.
# num=int(input())
# l=[]
# while num>0:
#     ld=num%10
#     l.append(ld)
#     num=num//10


# new=[]
# for i in l:
#     mul=1
#     for j in range(1,i+1):
#         mul*=j
#     new.append(mul)
# print(sum(new))


# armstrong
# input=int(input())
# inp=input
# a=0
# l=[]
# while input>0:
#     l.append(input%10)
#     input//=10
#     a+=1
# nl=[]
# for i in l:
#     nl.append(i**a)
# if inp==sum(nl):
#     print(True)
# else:
#     print(False)
# print(chr(ord('b')+1))
# a=input()
# l=a.split()
# new=[]
# for i in l:
#     new.append(i[::-1])
# print(" ".join(new))

# sarah
# def tuprev(s):
#     a=list(s)
#     print( tuple(a[::-1]))

# s=tuple(map(int,input().split(",")))
# tuprev(s)


# 2 find the highest
# def highest(s):
#     a=s[0]
#     for i in s:
#         if i>a:
#             a=i
#     print(a)

# s= tuple(map(int,input().split()))
# highest(s)


# 3 sofia search
# def find(a,hell):
    
#     if a in hell.keys():
#         print(hell[a])


# hell={'apple':'red','banana':'yellow', 'orange':'orange'}
# find(input().lower(),hell)


# 4
