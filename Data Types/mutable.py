# mutable:-once value is created it can be change the value

a=[10,30,45,56]
b=a
print(a)
print(b)
print("After changing the value")
a.append(49)
print(a)
print(b)