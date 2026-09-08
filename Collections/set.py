set1={1,2,2,3,4,5,6,7,8,9}
set2={1,2,3,4,5}

# #example1
# set1.add(10)
# print(set1)
# #---o/p---#
# "{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}"

# #example2
# set1.update([11,12,13])
# print(set1)

# #example3
# set1.remove(13)
# print(set1)
# #---o/p---#
# "{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}"

# #example4
# set1.discard(10)
# print(set1)
# #---o/p---#
# "{1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12}"

# #example5
# set2.pop()
# print(set2)
# #----o/p---#
# "{2, 3, 4, 5}"

# #example6
# set1.clear()
# print(set1)
# #---o/p---#
# "set()"

#example for mathematical operations on sets

#example7
# set3=set1.union(set2)
# print(set3)
#--o/p---#
"{1, 2, 3, 4, 5, 6, 7, 8, 9}"

# #example8
# set4=set1.intersection(set2)
# print(set4)
# #---o/p---#
# "{1,2,3,4,5}"

# #example9
# set5=set1.difference(set2)
# print(set5)
# #---o/p--#
# "{8, 9, 6, 7}"

#example10
set6=set1.symmetric_difference(set2)
print(set6)
#---o/p--#
"{6,7,8,9}"

#example11
set7=set1.isdisjoint(set2)
print(set7)
#---o/p--#
"False"

#example12
set8=set1.issuperset(set2)
print(set8)
#---o/p--#
"True"

#example13
set9=set2.issubset(set1)
print(set9)
#---o/p---#
"True"