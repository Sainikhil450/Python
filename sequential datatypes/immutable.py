# memory sharing example code
# memory sharing :- variable holding same value refer to same memory location.
a="orange"
b="orange"
print(id(a))
print(id(b))
a="apple"
print("the value store in different address :",id(a))

print("********************************************************")

# immutable :- once value is created we can't change the value
# If a variable is assigned an immutable object,
# the value of that object cannot be changed after assignment.
a1=(10,20,30,40)
b1=a1
print(a1)
print(b1)
print("After changing the value")
a1=(10,30,25,46)

print(a1)
print(b1)