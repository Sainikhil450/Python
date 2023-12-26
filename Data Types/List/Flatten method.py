list1=[23,[1,2,3],43,56,[12,40]]
l=[]
for i in list1:
    if type(i)==list or type(i)==tuple:
        for j in i:
            l.append(j)
    else:
        l.append(i)
print("flatten list:-",l)