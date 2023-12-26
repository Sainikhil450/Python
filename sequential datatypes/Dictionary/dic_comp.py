clist=["blue","green","yellow","red"]
dic={}
for i in clist:
    print(i)
    print(i[0])
    dic[i[0]]=i
print(dic)

print("*****************************")

d1={j[0]:j for j in clist}
print(d1)
