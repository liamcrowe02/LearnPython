#Input
x = int(input("Enter first input: "))
y = int(input("Enter second input: "))
z = x + y

#Output
print(z)
print(type(z))
print("liam", end="@")
print("gmail.com")
print("25", "01", "2002", sep="-")

a, b, c = [float(x) for x in input("Enter the three values separated by spaces: ").split()]
print(a)
print(b)
print(c)

# taking two inputs at a time
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
