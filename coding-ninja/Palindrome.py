
def reverse(num):
    rev = 0
    while num > 0:
        rem = num % 10
        rev = rem + (rev * 10)
        num = num // 10
    return rev

def isPalindrome(num):
    val2 = reverse(num)
    return val2 == num

value = int(input())
if isPalindrome(value):
    print("true")
else:
    print("false")