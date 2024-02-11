name = input("Enter your name please: ")
gender = input("Enter gender please: ")
age = int(input("Enter age please: "))

if (gender == "male" and age > 18.0):
    print("Hi " + name.capitalize() + " You are a " + gender + " and " + str(age) + " years old")
elif(gender == "female" and age > 18.0):
    print("Hi " + name.upper() + " You are a " + gender + " and " + str(age) + " years old")
else:
    print("Hi " + name + " You are underage")

