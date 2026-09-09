#------TYPE CONVERSION-----#

#---IMPLICIT TYPE CONVERSION-----#
num_int=10
num_float=2.5
result=num_int+num_float
print(result)
#---O/P----#
#---12.5----#

print(type(result))
#---O/P----#
#---<class 'float'>----#

#---EXPLICIT TYPE CONVERSION-----#
#example 1
num_str='10'
num_int=int(num_str)
print(num_int)
#---O/P----#
#---10----#

#---type of num-----#
print(type(num_str))
print(type(num_int))
#---O/P----#
"""<class 'str'>
<class 'int'>
"""
#example 2
name="shashank"
num_int=10
result=name+str(num_int)
print(result)

#---O/P----#
#---shashank10----#

#----type of result-----#
print(type(result))
#---O/P----#
#---<class 'str'>----#

#example 3
num_int=10
num_float=float(num_int)
print(num_float)
#---O/P----#
#---10.0----#

#type of num_float
print(type(num_float))
#---O/P----#
#---<class 'float'>----#

#example 4
num_float=2.5
num_int=int(num_float)
print(num_int)
#---O/P----#
#---2----#

#type of num_int
print(type(num_int))
#---O/P----#
#---<class 'int'>----#


num_str="10.5"
num_float=float(num_str)
print(num_float)
#---O/P----#
#---10.5----#

#type of num_float
print(type(num_float))
#---O/P----#
#---<class 'float'>----#

#example 5
num_float=2.5
num_str=str(num_float)
print(num_str)
#---O/P----#
#---2.5----#


#type of num_str
print(type(num_str))
#---O/P----#
#---<class 'str'>----#



#example 6

num_str="10.5"
num=int(num_str)
print(num)
#---O/P----#
#---ValueError: invalid literal for int() with base 10: '10.5'----# 

