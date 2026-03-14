
# mylistt = ["dHRUV", "Amit", "Suresh", "Neha", "Priya", 10, 25,6.4343]
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
 
 