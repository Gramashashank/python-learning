#EXample for the list Methods
#example1
my_list=input("enter the list of fruits names:").split(" ")
print(my_list)
#----o/p-----#
"""enter the list of fruits names:guava mango apple kiwi grape
['guava', 'mango', 'apple', 'kiwi', 'grape']"""

#example2
my_list1=[23,24,21,20,25,18,22,19,22,23]
#example3
my_list1.append(26)
print(my_list1)
#----o/p---#
"[23, 24, 21, 20, 25, 18, 22, 19, 22, 23, 26]"

#example4
my_list1.extend([18,19,27,28])
print(my_list1)
#----o/p---#
"[23, 24, 21, 20, 25, 18, 22, 19, 22, 23, 26, 18, 19, 27, 28]"

#example5
my_list1.sort()
print(my_list1)
#----o/p---#
"[18, 19, 19, 20, 21, 22, 22, 23, 23, 24, 25, 26, 27, 28]"

#example6
my_list1.sort(reverse=True)
print(my_list1)
#----o/p---#
"[28, 27, 26, 25, 24, 23, 23, 22, 22, 21, 20, 19, 19, 18, 18]"

#example7
my_list1.reverse()
print(my_list1)
#----o/p---#
"[18, 18, 19, 19, 20, 21, 22, 22, 23, 23, 24, 25, 26, 27, 28]"

#example8
copiedlist=my_list1.copy()
print(copiedlist)
#----o/p---#
"[18, 18, 19, 19, 20, 21, 22, 22, 23, 23, 24, 25, 26, 27, 28]"

res=my_list1.count(22)
print(res)
#----o/p---#
"2"

res1=my_list1.index(22)
print(res1)
#----o/p---#
"6"

my_list2=[["rama",200],
          ["shashank",300],
          ["jayanth",400]]
print(my_list2[2][1])
#----o/p---#
"400"