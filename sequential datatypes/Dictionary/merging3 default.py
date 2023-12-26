from itertools import chain
d1={"b":"blue","c":"car","y":"yellow"}
d2={'a':100,'x':200,"p":"python"}

d=dict(chain(d1.items(),d2.items()))
print(d)