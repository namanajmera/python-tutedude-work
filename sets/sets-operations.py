# Sets are non-sequential collections of items
# comma separated enclose with {}
# Sets can't contain duplicates elements.
# We can not use the list and tuple in sets.


s1 = {10, "Naman", 22.0}
print(s1)

s2 = {12,34,21,12,34,44.4,12}
print(s2)
print(len(s2))

s3 = {12,11,13,41}
s3.add(10)
s3.remove(11)
s3.discard(12)
s3.discard(18)
print(s3)

student1 = {"English", "Math", "Physics", "Chemistry"}
student2 = {"English", "Math", "Physics", "Biology"}
student3 = {"Sanskrit", "Hindi"}

# Intersection
print(student1.intersection(student2))
print(student1 & student2)

# Union
print("|", student1 | student2)
print(student1.union(student2))

# Difference
print(student1.difference(student2,student3))
print(student1 - student2 - student3)

