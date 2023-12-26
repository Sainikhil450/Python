# using forloop extract values from list
l1=[100,200,300,400,500]
print("using forloop to read list:-")
for i in l1:
    print(i)
print("********************************************")

#using index to read list
l2=["apple","mango","orange","grapes"]
x=l2[1]
x1=l2[-1]
print("positive index:-",x)
print("negative index:-",x1)

print("***********************************************")
# slicing to read list
l3=["apples",20,"price",230,"age",25]
a=l3[1:4:1]
a1=l3[-1:-5:-1]
print("positive slicing:-",a)
print("negative slicing:-",a1)


