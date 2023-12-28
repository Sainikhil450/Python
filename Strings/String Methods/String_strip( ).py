# Strip()
string1="******i love my india*********"
print("original strig:-",string1)
str_strip=string1.strip()
print("after apply strip:-",str_strip)

str1=string1.strip("*")
print("after apply strip:-",str1)

str2=string1.rstrip("*")
print("after apply strip:-",str2)

str3=string1.lstrip("*")
print("after apply strip:-",str3)