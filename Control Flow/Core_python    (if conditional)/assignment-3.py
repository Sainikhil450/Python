a=input("enter 4 values:")
num=a.split()
print(num)
total=int(num[0])+int(num[1])+int(num[2])+int(num[3])
print("total value :",total)
avg=total/len(num)
print(avg)
if avg>=80:
    print("Grade A")
elif avg>=60 and avg<80:
    print("Grade B")
elif avg>=40 and avg<60:
    print("Grade C")
else:
    print("FAIL")
#print("avg value : ",r)



