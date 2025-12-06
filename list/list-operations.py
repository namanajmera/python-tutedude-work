# Slicing
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(len(l1))
print(l1[1:8:1])

print(l1[1:8:2])

#  Concat
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l3 = [11, 12, 13, 14, 15, 16, 17, 18, 19,20]

print(l2 + l3)

# Repetition
print(l2 * 3)

# Appends
l1.append(12)
print(l1)

l1.insert(1, 12)
print(l1)

fruits = ["apple", "banana", "cherry"]
print(fruits)
fruits.extend(["orange", "apple", "pear"])
print(fruits)
fruits.append(["orange", "apple", "pear"])
print(fruits)
fruits.remove("orange")
print(fruits)
fruits.remove(["orange", "apple", "pear"])
print(fruits)
fruits.pop(2)
print(fruits)