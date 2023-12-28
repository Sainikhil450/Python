# # Uppercase() :- Converts a string into upper case
print("**************** UPPER CASE ********************")
Str1="i am nikhil,i am from vijayawada"
print("original String:-",Str1)
upper_case=Str1.upper()
print("small word convert into capital:-",upper_case)
#isupper():-Returns True if all characters in the
# string are upper case
a="MY NAME IS PAVAN"
if a.isupper():
    print("True")
else:
    print("False")
print()
print("**************** LOWER CASE ********************")
# Lower Case( ):Converts a string into lower case
str2="MY NAME IS NIKHIL"
print("ORIGINAL STRING:-",str2)
lower_case=str2.lower()
print("capital words convert into small:-",lower_case)
# islower()	Returns True if all characters in the
# string are lower case
a="welcome to vijayawada"
if a.islower():
    print("True")
else:
    print("False")