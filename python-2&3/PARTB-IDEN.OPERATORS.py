#ISWARYA
#Task B7.1-IDEN.OPERATORS

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 == list2)
print(list1 is list2)
print(list1 is list3)
print(id(list1), id(list2), id(list3))

#output:
#True
#False
#True
#1676489095360 1676444093504 1676489095360
