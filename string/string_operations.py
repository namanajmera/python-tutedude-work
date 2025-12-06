## Memberships Operations

# in
s1 = "Python is awesome"
isValid = "Python" in s1

print(isValid)
print("i" in s1)
print("z" in s1)

# not in

print("z" not in s1)

# Counting string from a string

s1 = "We are learning Python, And Python is awesome"
s2 = "e"

print(f"Occurrences of {s2} is {s1.count(s2)}")

print(s1.capitalize())
print(s1.upper())
print(s1.lower())
print(s1.swapcase())
print(s1.title())
print(s1.startswith("We"))