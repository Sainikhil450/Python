d1={"b":"blue","c":"car","y":"yellow"}
d2={'a':100,'x':200,"p":"python"}
d={**d1,**d2}
print(d)
print("***********************************")

r=dict(**d1,**d2)
print(r)