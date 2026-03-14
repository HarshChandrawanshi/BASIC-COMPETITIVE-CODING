
# mylistt = ["harsh", "Amit", "Suresh", "Neha", "Priya", 10, 25,6.4343]
# print(mylistt)
# print(type(mylistt))
# print(mylistt[0])
# print(mylistt[2:4])
# print(mylistt[-1])
# print(mylistt[1:8:2])
# print(mylistt[:5])
# print(mylistt[::-1])
# ['dHRUV', 'Amit', 'Suresh', 'Neha', 'Priya', 10, 25, 6.4343]
# <class 'list'>
# dHRUV
# ['Suresh', 'Neha']
# 6.4343
# ['Amit', 'Neha', 10, 6.4343]
# ['dHRUV', 'Amit', 'Suresh', 'Neha', 'Priya']
# [6.4343, 25, 10, 'Priya', 'Neha', 'Suresh', 'Amit', 'dHRUV']
# mylistt.append(4)
# mylistt.append("break")
# print(mylistt)
# mylistt.insert(1,"continue")
# print(mylistt)
# mylistt.remove("Amit")
# print(mylistt)
# ['dHRUV', 'Amit', 'Suresh', 'Neha', 'Priya', 10, 25, 6.4343, 4, 'break']
# ['dHRUV', 'continue', 'Amit', 'Suresh', 'Neha', 'Priya', 10, 25, 6.4343, 4, 'break']
# ['dHRUV', 'continue', 'Suresh', 'Neha', 'Priya', 10, 25, 6.4343, 4, 'break']
# newlistt= mylistt.copy()
# print(newlistt)
# ['dHRUV', 'continue', 'Suresh', 'Neha', 'Priya', 10, 25, 6.4343, 4, 'break']
# mylist_ = [
#     ["rudram",
#         [4, 5, 6]
#     ],
#     [
#         [7, 8, 9],
#         [10, 11, 12]
#     ]
# ]
# print(mylist_)
# print(mylist_[0][1])
# print(mylist_[1][0])
# print(mylist_[1][1])
# #print(mylist_[2][1])
# #print(mylist_[2][0])
# [['rudram', [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
# [4, 5, 6]
# [7, 8, 9]
# [10, 11, 12]
# list1=["rd "," vd"]
# list2=[1,2,4]
# list3=list1+list2
# print(list3)
# del list2[2]
# print(list2)
# list2.clear()
# print(list2)
# name="rudram"
# print(name)
# my=list(name)
# print(my)
# ['rd ', ' vd', 1, 2, 4]
# [1, 2]
# []
# rudram
# ['r', 'u', 'd', 'r', 'a', 'm']
# gh=[21,32,1,2,6]
# gh.sort()
# print(gh)
# [1, 2, 6, 21, 32]
# maths=10
# phy =10
# print(id(maths))
# print(id(phy))
# 11654664
# 11654664
# mylistq=[32,12,43,53]
# newlistq=mylistq
# print(id(mylistq))
# print(id(newlistq))
# 135439529511104
# 135439529511104
# print('Z' in name)
# False
# for i in range (1,6,2):
#     print(name+"+")
#     print(i)
# rudram+
# 1
# rudram+
# 3
# rudram+
# 5
# for i in range (5,0,-1):
#     # print(name+"+")
#     print(i)
# 5
# 4
# 3
# 2
# 1
# for i in range (1,11):
#     print(i*2,"",i*3,"",i*5)
# 2  3  5
# 4  6  10
# 6  9  15
# 8  12  20
# 10  15  25
# 12  18  30
# 14  21  35
# 16  24  40
# 18  27  45
# 20  30  50
# no = int(input("enter numbers"))
# if no>0:
#     print("number is pos")
# if no<0:
#     print("number is neg")
# if no==0:
#     print("number is zero")
# day = input("enter")

# if day == "sunday" or"saturday":
#     print("non working day")
# else:
#     print("working day")
# m1 = int(input("enter numbers"))
# m2 = int(input("enter numbers"))
# m3 = int(input("enter numbers"))
# per=(m1+m2+m3)/300*100
# print(per)
# if per>60:
#     print("ellibable")
# else:
#     print("not ellible")
# n1 = int(input("enter numbers"))
# n2 = int(input("enter numbers"))
# n3 = int(input("enter numbers"))
# n4 = int(input("enter numbers"))
# n5 = int(input("enter numbers"))

# if n1 >= n2 and n1 >= n3 and n1 >= n4 and n1 >= n5:
#     print("max:", n1)
# elif n2 >= n1 and n2 >= n3 and n2 >= n4 and n2 >= n5:
#     print("max:", n2)
# elif n3 >= n1 and n3 >= n2 and n3 >= n4 and n3 >= n5:
#     print("max:", n3)
# elif n4 >= n1 and n4 >= n2 and n4 >= n3 and n4 >= n5:
#     print("max:", n4)
# else:
#     print("max:", n5)
 
 
#class 3
# mydict={
#   101:"harsh",
#   102:"Ahish",
#   "103":"mohinhsh",
#   "104":"runwal",
#   101:"ashish",
#   104:"Ashish"

# }
# print(mydict)
     
# {101: 'ashish', 102: 'Ahish', '103': 'mohinhsh', '104': 'runwal', 104: 'Ashish'}

# a =mydict[101]
# print(a)
     
# ashish

# mydict[102]="peter"
# print(mydict)
     
# {101: 'ashish', 102: 'peter', '103': 'mohinhsh', '104': 'runwal', 104: 'Ashish'}

# for x in mydict:
#   print(x)
     
# 101
# 102
# 103
# 104
# 104

# for x in mydict.values():
#   print(x)
     
# ashish
# peter
# mohinhsh
# runwal
# Ashish

# for x,y in mydict.items():
#   print(x,y)
     
# 101 ashish
# 102 peter
# 103 mohinhsh
# 104 runwal
# 104 Ashish

# mydict["mobile_no"]=999881100
# print(mydict)
     
# {101: 'ashish', 102: 'peter', '103': 'mohinhsh', '104': 'runwal', 104: 'Ashish', 'mobile_no': 999881100}

# mydict={101:"dhruv","proffesional":"developer","empid":1001}
# mydict.pop(101)
# print(mydict)
     
# {'proffesional': 'developer', 'empid': 1001}

# name ="dhruvrunwal"
# print(name[0])
# print(name[1])
# print(name[-1])
# print(name[0:5])
# print(name[1:])
# print(name[:5])
# print(name[:])
# print(name[1:8:2])
# print(name[::-1])
     
# d
# h
# l
# dhruv
# hruvrunwal
# dhruv
# dhruvrunwal
# hurn
# lawnurvurhd

# s="helpcode is best platform for coding practising programming"
# print(s.find("helpcode"))
# print(s.find("python"))
# print(s.find("programming"))
     
# 0
# -1
# 48

# s="prashant","asish","sandip"
# m='|'.join(s)
# print(m)
     
# prashant|asish|sandip

# s ="python is a high level programming language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

     
# python is a high level programming language
# PYTHON IS A HIGH LEVEL PROGRAMMING LANGUAGE
# PYTHON IS A HIGH LEVEL PROGRAMMING LANGUAGE
# Python Is A High Level Programming Language
# Python is a high level programming language

# print('Subject Marks')
# phy =50
# chem=60
# math=70
# print("physics={} chemistry ={} maths={} ".format(phy,chem,math))
# print("physics={0} chemistry ={1} maths={2} ".format(phy,chem,math))
# print("physics={x} chemistry ={y} maths={z} ".format(x=phy,y=chem,z=math))

# total=phy+chem+math
# print("total marks={}".format(total))
# print("rollno,","7".zfill(4))
     
# Subject Marks
# physics=50 chemistry =60 maths=70 
# physics=50 chemistry =60 maths=70 
# physics=50 chemistry =60 maths=70 
# total marks=180
# rollno, 0007

# print('prashantjha777'.isalnum()) #True

# print('prashantjha.isalpha()) #True

# print('777f'.isdigit())

# print('sdsdsdsd.islower())

# print(".islower())

# print("PRASHANT)'.isupper())

# print('My Name Is Prashant.istitle())

# print(".istitle())

# print(".isspace())

# print("Hello".startswith("He"))

# print("Hello".endswith("lo"))
     
#   File "/tmp/ipykernel_223/3486786587.py", line 3
#     print('prashantjha.isalpha()) #True
#           ^
# SyntaxError: unterminated string literal (detected at line 3)


     

# print('prashantjha777'.isalnum()) #True

# print('prashantjha'.isalpha()) #True

# print('777f'.isdigit())

# print('sdsdsdsd'.islower())

# print(' '.islower()) # Assuming the intent was to check an empty string or space

# print("PRASHANT".isupper())

# print('My Name Is Prashant'.istitle())

# print('My Name Is Prashant'.istitle()) # Corrected to show a proper title case string

# print('  '.isspace())

# print("Hello".startswith("He"))

# print("Hello".endswith("lo"))
     
# True
# True
# False
# True
# False
# True
# True
# True
# True
# True
# True

# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d)
# print((a-b)*(c/d))
# print(a+(b*c)/d)
     
# 160.0
# 40.0
# 110.0

# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x!=z)
     
# True
# False
# True

# name ="dhruv"
# data=['a','i','e','o','u']
# vow=0
# con=0
# for i in  name :


#     if i in data:
#         vow+=1
#     else:
#         con+=1
#     print(i)
# print("no. of vowels",vow)
# print("no. of consonats",con)

     
# d
# h
# r
# u
# v
# no. of vowels 1
# no. of consonats 4






#class 4


#  for i in range(1,5):
#      if i==3:
#          break
#      print(i)
     
# 1
# 2

# for i in range(1,5):
#    if i==3:
#     continue
# print(i)
     
# 4

# for i in range(5,0,-1):
#     if i==3:
#         continue
#     print(i)
     
# 5
# 4
# 2
# 1

# for i,j in zip (range(1,6),range(5,0,-1)):
#   if i==3 and j==3:
#      continue
#   print(i," ",j)

     
# 1   5
# 2   4
# 4   2
# 5   1

# i=1
# while i<=5:
#   print(i)
#   i=i+1
     
# 1
# 2
# 3
# 4
# 5

# username=""
# password=""

# while username !="Admin" and password != "hello":
#     username=input("Enter username: ")
#     password=input("Enter password: ")

     
# Enter username: dhruv
# Enter password: heineA
# Enter username: JNDJAN
# Enter password: XJXAX
# Enter username: ADMIN
# Enter password: HELLO'
# Enter username: Admin 
# Enter password: hello

# n=int(input("enter number"))
# sum=0
# i=1
# while i<=n:
#   sum=sum+i
#   i=i+1
# print("the sum of ",n,"numbers is :",sum )

     
# enter number5
# the sum of  5 numbers is : 15

# name = input("enter your name ")
# newname=""
# for i in name:
#   if i not in newname:
#      newname +=i
# print("old name :",name)
# print("the new name is :",newname)
     
# enter your name Dhruv Runwal
# old name : Dhruv Runwal
# the new name is : Dhruv Rnwal

# #write a program to REVERSE A string usning loop
# name = input("enter your name ")
# newname =""
# for i in name :
#     newname =i+newname
# print("the reversed string is:",newname)
     
# enter your name reversed
# the reversed string is: desrever

# mycart =[10,20,200,300,800,60,500]
# for i in  mycart:
#   if i >400:
#     print("this my  purchased cart item ")
#     continue
#   print(i)
     
# 10
# 20
# 200
# 300
# this my  purchased cart item 
# 60
# this my  purchased cart item 

# string=input("enter A string ")
# newname =""
# for i in string :
#     newname = i+newname

# if (newname == string):
#   print("the sttring is pallindrome")
# else:
#   print("not pallindrome not  pallindrome")

# print("the reversed string is:",newname)

     
# enter A string racecar
# the sttring is pallindrome
# the reversed string is: racecar

# #write a program to check the if two srtrings are anagram of each other
# #check if the character counts in both srings are the same
# #sample listen silent

# string1=input("enter 1st string :")
# string2=input("enter 2nd string :")


# s1=string1.lower()





     

# mydict = {}
# mydict['name'] = 'Alice'
# mydict['age'] = 30
# mydict['city'] = 'New York'

# print(mydict)
     
# {'name': 'Alice', 'age': 30, 'city': 'New York'}


     

# my_dictionary = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# # Check if 'name' key exists
# if 'name' in my_dictionary:
#     print("The key 'name' exists in the dictionary.")
# else:
#     print("The key 'name' does NOT exist in the dictionary.")

# # Check if 'country' key exists
# if 'country ' in my_dictionary:
#     print("The key 'country' exists in the dictionary.")
# else:
#     print("The key 'country' does NOT exist in the dictionary.")
     
# The key 'name' exists in the dictionary.
# The key 'country' does NOT exist in the dictionary.

# #nested for loop
# for i in range(1,5):
#   for j in range(1,5):
#     print(i,end= " ")
#   print()



     
# 1 1 1 1 
# 2 2 2 2 
# 3 3 3 3 
# 4 4 4 4 

# n = int(input("enter a number of rows"))
# for i in range(1,n+1):
#   for j in range(1,n+1):
#     print(chr(64+i),end=" ")
#   print()
     
# enter a number of rows5
# A A A A A 
# B B B B B 
# C C C C C 
# D D D D D 
# E E E E E 

# n = int(input("enter a number of rows"))
# for i in range(1,n+1):
#   for j in range(1,n+1):
#      print(n+1-i,end=" ")
#   print()
     
# enter a number of rows5
# 5 5 5 5 5 
# 4 4 4 4 4 
# 3 3 3 3 3 
# 2 2 2 2 2 
# 1 1 1 1 1 

# n = int(input("enter a number of rows"))
# for i in range(1,n+1):
#   for j in range(1,i):
#     print(j,end=" ")
#   print()
     
# enter a number of rows6

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

# n = int(input("enter a number of rows"))
# for i in range(1,n+1):
#   for j in range(1,n+2-i):
#     print("*",end=" ")
#   print()
     
# enter a number of rows6
# * * * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# n = int(input("enter a number of rows"))
# for i in range(1,n+1):
#   for j in range(1,n+2-i):
#     print(chr(64+i),end=" ")
#   print()
     
# enter a number of rows6
# A A A A A A 
# B B B B B 
# C C C C 
# D D D 
# E E 
# F 