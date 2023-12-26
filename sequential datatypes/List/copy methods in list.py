# copy:- it is a process of duplicating values
# from one variable to another variable .
# 1.reference copy
import copy

list1=[1,2,34,56,67]
list2=list1
print("original list:-",list1)
print("reference copy list:-",list2)
print("original list address",id(list1))
print(id(list2))

# 2.shallow copy
# it stores values in different memory location
l1=[20,30,40,60,45]
l2=l1.copy()
print("original list:-",l1)
print("shallow copy list:-",l2)
print("original list address",id(l1))
print(id(l2))

# 3.deep copy
l3=[20,["a","b"],30,40,60,45]
l4=copy.deepcopy(l3)
print("original list:-",l3)
print("deep copy copy list:-",l4)
print("original list address",id(l3))
print(id(l4))
