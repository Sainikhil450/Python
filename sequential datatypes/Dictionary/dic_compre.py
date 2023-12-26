list1=["usa","india","france","uk","uae","japan","russia","america","geramany"]
dic={}
print(list1)
for i in list1:
    if len(i)>=5:
        dic[i[0]]=i
print(dic)