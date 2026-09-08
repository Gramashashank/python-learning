#Example for tuple methods


my_tuple=("A","A","B","C","D","A","B","C","D")
#example1
print(my_tuple.count("A"))
#----o/p---#
"3"

#example2
print(my_tuple.count("B"))
#----o/p---#
"2"

#example3
print(my_tuple.count("C"))
#----o/p---#
"2"

#example4
print(my_tuple.count("D"))
#----o/p---#
"2"

#example5
print(my_tuple.index("A"))
#----o/p---#
"0"

#example6
print(my_tuple.index("B"))
#----o/p---#
"2"

#example7
print(my_tuple.index("C"))
#----o/p---#
"3"

#example8
print(my_tuple.index("D"))
#----o/p---#
"4"

#example9
print(len(my_tuple))
#---o/p--#
"9"

#example10
my_tuple1=(50,21,35,88,90,97)
print(max(my_tuple1))
#----o/p---#
"97"

#example11
print(min(my_tuple1))
#----o/p---#
"21"

#example12
print(sum(my_tuple1))
#----o/p---#
"381"

#example13
print(sorted(my_tuple1))
#----o/p---#
"[21, 35, 50, 88, 90, 97]"