#Lists
lists = [1, 2, 1, "Hello", "World", True, 1.56]
print(lists)
print(lists[0])
print(lists[-1])
print(lists[1:3])

if "Hello" in lists:
    print("Yes it is")

lists[0] = "Liam"
lists[1:3] = ["blackcurrant", "watermelon"]
lists.append(100)
lists.insert(4, "orange")
print(lists)
lists.remove("blackcurrant")
print(lists)

#contructor lists
thisLists = list(("apple", "cherry", "banana"))
print(thisLists)

#Tuples
tuples = ("apple", "banana", "cherry")
print(tuples)
print(len(tuples))
#As above they are the same in lists and tuples

#Update, add, remove tuple: You need to convert the tuple to list and then back once the change is made.
x = (1, 3, 4, 6)
y = list(x)
y[1] = "String"

x = tuple(y)
print(x)
for i in range(len(tuples)):
    print(tuples[i])

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i+1 #i++ does not exist in Python

#Sets

#Dictionaries