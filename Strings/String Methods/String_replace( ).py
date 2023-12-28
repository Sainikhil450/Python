str2="Welcome to python world"
print("original string:-",str2)
replace_str1=str2.replace("python","java")
print(replace_str1)

print("**************************************************")
print()
str1="""java is object oreinted language
        java is a popular language
             i am java devloper """
print("original String",str1)
res=str1.replace("java devloper","python devloper")
print(res)
r=res.replace("java","python",1)
print(r)
res1=res.replace("java is a","python is a")
print(res1)
res2=str1.replace("java is a","python is a")
print(res2)