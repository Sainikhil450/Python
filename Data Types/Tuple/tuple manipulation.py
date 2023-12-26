tup1=("python",200,"data science",200,60,23.33)
print(tup1)
print("*********************************")
print(tup1[3])
#tup1[3]=500 #error
#print(tup1)
tup_list=list(tup1)
print(tup_list)
tup_list[3]=500
print(tup_list)
del tup_list[5]
print(tup_list)
tup1=tuple(tup_list)
print(tup1)