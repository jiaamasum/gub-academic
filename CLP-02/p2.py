#Set: Find the common elements between two lists using sets.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

elements = set(list1) & set(list2)

print(elements)