# List is mutable
l1=[10,20,40,56,"sai"]
l2=l1
print("original values of l1:-",l1)
print("original values assign to l2:-",l2)
print("-*********************************-")
print("after change the l1 values ")
l1.append([1,2,3])
print("l1 values are changes",l1)
print("it is also reflected:-",l2)