# Slicing :- It is a process of Extracting substring
# from main string is called Slicing

# Slicing is three main components :
# Starting index:-Starting index of the substring
# Ending index:-Ending index of the substring add with extra index
# step :-Process of displaying extracted substring

# Slicing syntax:- str[<starting index>:<ending index>:<step>]

# Positive Slicing:-
# Staring index ==> 0
# Ending index  ==> [ :len(str): ]
# step ==>positive one or anything  it is default it can take
# Starting index < ending index

str1="Welcome our Python World"
print("Original string:-",str1)

print("*************** Positive Slicing *********************")

str_ind=str1[1:len(str1):1]
print("starting positive slicing value:-",str_ind)

# Negative Slicing:
# default Staring index ==> -1
# default Ending index  ==> [ :-(len(str)+1): ]
# step ==>-1
# Starting index > ending index

print("*************** Negative Slicing *********************")

str_index=str1[-1:-21:-1]
print("ending negative Slicing value:-",str_index)


