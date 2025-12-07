import copy

l1 = [1, 2, 3, [4, 5, 6]]
l2 = copy.copy(l1)
l3 = l1
l4 = copy.deepcopy(l1)
# print(l1)
# print(l2)
# print(l3)
#
# print("l1 ==> ", id(l1))
# print("l2 ==> ", id(l2))
# print("l3 ==> ", id(l3))

l1[0] = 11
l1[3][0] = 22

print(l1)
print(l2)
print(l3)
print(l4)

print("l1 ==> ", id(l1))
print("l2 ==> ", id(l2))
print("l3 ==> ", id(l3))
print("l4  ==> ", id(l4))
