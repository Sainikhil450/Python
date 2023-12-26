#merging to two dictionary using collection
from collections import ChainMap
d1={"b":"blue","c":"car","y":"yellow"}
d2={'a':100,'x':200,"p":"python"}
d=dict(ChainMap(d1,d2))
print(d)