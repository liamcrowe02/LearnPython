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

thisLists = list(("apple", "cherry", "banana"))
print(thisLists)