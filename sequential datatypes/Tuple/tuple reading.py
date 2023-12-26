tup1=("python",200,"data science",60,23.33)
for i in tup1:
    print(i)
    if type(i)==str:
        for j in i:
            print(j)
print("***********************************")
#nested forloop

for i in tup1:
    print(i)
    if type(i)==str:
        for j in i:
            print(j)