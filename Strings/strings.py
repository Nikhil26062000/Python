

#? string is immutable 

str1 = "This is nik's lappi"
str2 = 'hello this string \nwill be in multiline'
str3 = """Hie I a m Nik"""
str4 = 'hello this string \twill have some spaces'
str5 = "apple"

print(str1)
print(str2)
print(len(str3))
print(str4)
print(str3+" "+str4)

# slicing
print(str1[1:6])
print(str1[:3])
print(str1[3:])

#slicing (Negative index)
print(str5[-3:-1]) # -1 will be index of last char

print("Capitalize :",str4.capitalize()) 
print("Original string won't get affected :",str4)