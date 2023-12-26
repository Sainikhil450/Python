c={}
for i in range(1,30):
    if i%3==0:
        c[i]=i**3
print(c)

print("**************************")
dic={j:j**3 for j in range(1,29) if j%3==0}
print(dic)