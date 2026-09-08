#EXAMPLE OF STRING METHODS

#Example1
s="Python is easy to learn"
res=s.upper()
print(res)
#-----o/p----#
"PYTHON IS EASY TO LEARN"
#Example2
lower=s.lower()
print(lower) 
#----o/p----#
"python is easy to learn"
#Eample3
capital=s.capitalize()
print(capital)
#----o/p----#
"Python is easy to learn"
#exampl4
title=s.title()
print(title)
#----o/p----#
"Python Is Easy To Learn"
#examole4
swapcase=s.swapcase()
print(swapcase)
#----o/p----#
"pYTHON IS EASY TO LEARN"
#example5
center=s.center(30,"*")
print(center)
#---o/p---#
"***Python is easy to learn****"
#example6
find=s.find("y")
print(find)
#----o/p----#
1
#example7
isdecimal=s.isdecimal()
print(isdecimal)
#----o/p----#
False
#example8
isalnum=s.isalnum()
print(isalnum)
#----o/p----#
False
#example9
isalpha=s.isalpha()
print(isalpha)
#----o/p----#
False
#example10
split=s.split(" ")
print(split)
#----o/p----#
['Python', 'is', 'easy', 'to', 'learn']
#example11
replace=s.replace("Python","Java")
print(replace)
#----o/p----#
"Java is easy to learn"
#example12
strip=s.strip(" ")
print(strip)
#----o/p----#
"Python is easy to learn"
#example13
startswith=s.startswith("Python")
print(startswith)
#----o/p----#
True
#example14
endswith=s.endswith("learn")
print(endswith)
#----o/p----#
True
#example15
rfind=s.rfind("a")
print(rfind)
#----o/p----#
20
#example16
partition=s.partition(" ")
print(partition)
#----o/p----#
("Python", " ", "is easy to learn")
#example17
istitle=s.istitle()
print(istitle)
#----o/p----#
False
#example18
s1=""
join=s1.join(["Python","is","easy","to","learn"])
print(join)
#----o/p---#
"Python is easy to learn"
