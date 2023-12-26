# Zip function:- it accepts multiple iterable and
# combine them based on common index
l1=[10,20,30,40,50]
l2=[2,4,6,7,8]
lr=zip(l1,l2)
for i,j in lr:
    print(i)
    print(j)
    print("addition both l1 and l2:-",i+j)