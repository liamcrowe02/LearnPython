#For loop
fruit = ["apple", "banana", "cherry"]
for x in fruit:
    print(fruit)
    if x == "banana":
        break

#While
i = 0
while i < 6:
    i += 1
    if i == 6:
        break
    print(i)

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

i = 0
while i <= 10:
    print("Number", i)
    i = i+1
