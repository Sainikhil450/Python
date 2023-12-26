d1=dict((("b",("box","blue")),("c",("car","cap")),("y",("yummy","yellow"))))
print(d1)
for i in d1.values():
    print(i)
for k in d1.items():
    print(k)
for x,y in d1.items():
    print(x,end="==")
    print(y)