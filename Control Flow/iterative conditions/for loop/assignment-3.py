for i in range(3):
    std = input("enter the number:")
    res = std.split()
    total = int(res[0]) + int(res[1]) + int(res[2]) + int(res[3])
    print("TOTAL:", total)
    avg = total / len(res)
    print("AVERAGE:", avg)
    grade = ("grade A" if avg>= 80 else
            ("grade B" if avg>= 60 else
            ("grade c"if avg>=40 else "fail")))
    print(grade)
