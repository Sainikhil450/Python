#Split() :-	Splits the string at the specified separator,
# and returns a list
email="sai.nikhil2010@gmail.com"
res=email.split("@")
print(res)
res1=res[0].split(".")
print(res1)
print(res1[1])
print(len(res1[1]))
print(len(res1[1])-4)
#print(res1[1][10])
year=res1[1][len(res1[1])-4: :1]
print(year)
age=2023-int(year)
print(age)
print("fisrt name:",res1[0].title())
print("second name:",res1[1].title())
print("domain name:",res[1].capitalize())
print("age:",age)
