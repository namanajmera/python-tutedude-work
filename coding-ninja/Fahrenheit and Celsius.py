# Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W),
# you need to convert all Fahrenheit values from Start to End at the gap of W,
# into their corresponding Celsius values and print the table.
#
# Hint : Use type casting

S = int(input())
E = int(input())
W = int(input())

while S <= E:
    val1 = S
    val2 = (val1 - 32) / 1.8
    S+=W
    print(f"{val1} {int(val2)}")