#Ex 1: No need to specify the variable. x and y are both int's
x = 5
y = 20
print(x + y)

#Ex 2: Name is a string. String must be inside a '' or ""
name = "Liam"

#Ex 3: Casting, specify the variable. 'X' will not change 'x'
x = str(3)
X = float(3.14)
print(x, X)

#Ex 4: Getting the type of variable
x = 'c'
print(type(x))

#Ex 5: xyz are assigned one after other, and abc are all assign 100.1
x, y, z = 1, 2, 3
a = b = c = float(100.1)
print(x, y, z, a, b, c)

#Ex 6: Unpack a collection: assign each value in number to xyz in order.
number = [1, 2, 3]
x, y, z = number
print(x, y, z)

"""Ex 7: This is a global variable because it is not in the function (line 34 - 37)
   In the function global overwrites 'x' outside of function. Output: amazing
"""
x = ('Liam is studying python')
def _myFunction():
    global x
    x = "amazing"
    print(x)
_myFunction()

