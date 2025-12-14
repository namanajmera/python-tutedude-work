# Problem statement
# Given an integer n, find if n is positive, negative or 0.
#
# If n is positive, print "Positive"
#
# If n is negative, print "Negative"
#
# And if n is equal to 0, print "Zero".

value = int(input("Enter the number:- "))
if value == 0:
    print("Zero")
elif value >=1:
    print("Positive")
else:
    print("Negative")