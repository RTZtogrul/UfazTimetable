from newlist import NewList


a = NewList(1,2,3,4,5)

print(a[3])
print(a)

a.append(4)
print(a)

print(a.count(4))
print(a)

a.pop(3)
print(a)