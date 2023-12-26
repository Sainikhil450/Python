#append
list1=[10,12,14,16,18,20]
list1.append(10)
print("append single value:-",list1)
print("---------------------------------------------")
list2=[1,2,3,4,5]
list2.append([10,20,39,"nikki"])
print("append multiple values:-",list2)
print("*********************************************")

#extend
l1=[1,3,5,7,9]
l1.extend([26,"sai"])
print("extend value:-",l1)

print("*********************************************")
#insert
l2=[21,22,23,24,25]
l2.insert(1,28)
print("insert the values into list:-",l2)
print("-----------------------------------------------")
l3=[34,35,37,38,39]
l3[0:1:1]=[1,2,3]
print("insert multiple values into list:-",l3)