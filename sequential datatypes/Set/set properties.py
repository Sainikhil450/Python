# Hetrogenous values
s={10,"apple",34,"mango"}
print("hetrogenous values:-",s)
print("---------------------------------------------------")

# Duplicates are not allowed
s={10,20,30,40,10}
print("duplicates are not allowed:-s={10,20,30,40,10}")
print(s)
print("---------------------------------------------------")

# Order is not preserved
s1={10,40,56,23,12}
print("original :-s1={10,40,56,23,12}")
print("Order is not preserved:-",s1)
print("---------------------------------------------------")
# Mutable
s2={12,4,57,8,9}
r=s2
print("original set list:-",s2)
print("copy set list:-",r)
print("*****************************************")
s2.update([1,2,3])
print("update set list:-",s2)
print("copy set list:-",r)
print("---------------------------------------------------")

print("indexing and slicing is not possible")