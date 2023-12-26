staff=input("enter your role in school:")
staff=staff.upper()
exp=int(input("enter the year of exp"))
if staff=="PRINCIPLE":
    if exp>=10:
        print("hike is 15%")
    elif exp>=1 and exp<10:
        print("hike is 10%")
    else :
        print("hike is 0%")
elif staff=="HOD":
    if exp>=5:
        print("hike is 10%")
    elif exp>=1 and exp<5:
        print("hike is 5%")
    else:
        print("hike is 0%")
elif staff=="TEACHER":
    if exp>=10:
        print("hike is 8%")
    elif exp>=5 and exp<10:
        print("hike is 5%")
    else:
        print("hike is 2%")
else:
    if exp>=15:
        print("hike is 10%")
    elif exp>=5 and exp<15:
        print("hike is 5%")
    else:
        print("hike is 2%")