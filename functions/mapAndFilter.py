
# Filter
def odds(n):
    if n % 2 != 0:
        return True
    else:
        return False

filtered = filter(odds, range(1,11))
print(list(filtered))

def sqOfNumber(n):
    return n ** 2

mapped = map(sqOfNumber, range(1,11))
print(list(mapped))