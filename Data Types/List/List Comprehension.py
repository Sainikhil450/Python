# List comprehension:- creating a kist in single line
# syntax:-list=[(output expresion)(input sequence)(condition)]
l=[1,2,3,4,5]
r=[x+1 for x in l]
print(r)

print("********************************************")

res=[x for x in range(1,11) if x%2==0 ]
print(res)