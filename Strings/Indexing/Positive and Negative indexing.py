# Indexing:-it is a technique with which value are extracted
# from internal memory location from sequential data types.

# Indexing are two types:-
# 1.Positive indexing
# 2.Negative indexing

# Positive indexing:-
# direction of flow -->Left to Right
# Starting Index -->0
# Ending Index -->Len(str)-1
str1="Welcome to Vijayawada"
print("original String:-",str1)

print("***************** Positive Indexing ***************")

str_index=str1[0]
print("starting positive index value:-",str_index)

print("--************************************************************--")

print("last value index :-",len(str1)-1)
str_endindex=str1[20]
print("ending negative index value:-",str_endindex)

print("------------------------------------------------------------------")
# Negative indexing:-
# direction of flow --> Right to Left
# Starting Index --> -1
# Ending Index --> -len(str)
str2="My name is Nikhil"
print("Original string:-",str2)

print("***************** Negative Indexing ***************")

str_ind=str2[-1]
print("starting positive index value:-",str_ind)

print("--************************************************************--")

print("last value index :-",-len(str2))
str_end_index=str2[-17]
print("ending negative index value:-",str_end_index)