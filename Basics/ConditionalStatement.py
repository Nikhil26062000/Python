
color = input("Enter the color   :")
if(color == "green"):
    print("Go")
elif(color == "yellow"):
    print("look")
elif(color == "red"):
    print("stop")
else:
    print("Light is broken")


# ternary operator
food = input("Food is :")
eat = "yes" if food == "cake" else "no"
print(eat)

# ternary operator
num = int(input("Number is :"))
print("valid") if num == 18 or num ==20 else print("invalid") 

#clever If ternary operator

age = int(input("Age is :"))
vote = ("no","yes") [age>=18] # first will be flase value and second will be true i.e : "no" , "yes"
print(vote)

"""
If age is greater than or equal to 18, age >= 18 evaluates to True, which is equivalent to 1 in indexing. Therefore, ("no", "yes")[1] returns "yes".
If age is less than 18, age >= 18 evaluates to False, which is equivalent to 0 in indexing. Therefore, ("no", "yes")[0] returns "no".

"""