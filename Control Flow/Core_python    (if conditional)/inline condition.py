mark=int(input("enter the marks:"))
res="pass" if mark>=40 else "fail"
print(res)
print("***********************************")

dsg=input("enter your designation:")
dsg=dsg.upper()
res1="hike 25%" if dsg=="PM" else  "hike is 20%" if dsg=="TM" else "hike is 17%" if dsg=="testing" else "hike is 10%"
print(res1)

marks=int(input("enter the marks:"))
res2="GRADE A" if marks>=80 else "GRADE B" if marks>=60 and marks<80 else"GRADE C" if marks>=40 and marks<60 else "fail"
print(res2)
