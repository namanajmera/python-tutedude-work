str = input()

def isPalindrome(str):
    length = len(str)
    start = 0
    end = length - 1
    while start < end:
        if str[start] != str[end]:
            return False
        start += 1
        end -= 1
    return True

if isPalindrome(str):
    print("true")
else:
    print("false")