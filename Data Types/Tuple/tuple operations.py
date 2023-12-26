tup=(10,20,30,40,50)
tup2=(100,200,300,400,500)
res_list=[]
for i in range(5):
    print(tup[i])
    print(tup2[i])
    res=(tup[i]+tup2[i])
    print(res)
    res_list.append(res)
print(res_list)
tup1=tuple(res_list)
print(tup1)