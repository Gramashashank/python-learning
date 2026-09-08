#examples for dictionary methods
my_info={"Name":"Rama",
           "Age":22,
           "Gender":"Male",
           "Place":"Tirupati",
           "Qualification":"B.Tech"
           }
#example1
print(my_info.get("Name"))
print(my_info.get("Age"))
print(my_info.get("Gender"))
print(my_info.get("Place"))
print(my_info.get("Qualification"))
#---o/p---#
"""Rama
22
Male
Tirupati
B.Tech"""

#example2
print(my_info.keys())
#---o/p---#
"dict_keys(['Name', 'Age', 'Gender', 'Place', 'Qualification'])"

#example3
print(my_info.values())
#---o/p---#
"dict_values(['Rama', 22, 'Male', 'Tirupati', 'B.Tech'])"

#example4
print(my_info.items())
#---o/p---#
"dict_items([('Name', 'Rama'), ('Age', 22), ('Gender', 'Male'), ('Place', 'Tirupati'), ('Qualification', 'B.Tech')])"

#example5
my_info.pop("Qualification")
print(my_info)
#---o/p---#
"{'Name': 'Rama', 'Age': 22, 'Gender': 'Male', 'Place': 'Tirupati'}"

#example 6
my_info.popitem()
print(my_info)
#---o/p---#
"{'Name': 'Rama', 'Age': 22, 'Gender': 'Male'}"

#example 7
my_info.update({"Qualification":"B.Tech"})
print(my_info)
#---o/p---#
"{'Name': 'Rama', 'Age': 22, 'Gender': 'Male', 'Qualification': 'B.Tech'}"

#example 8
copied_dict=my_info.copy()
print(copied_dict)
#---o/p---#
"{'Name': 'Rama', 'Age': 22, 'Gender': 'Male', 'Qualification': 'B.Tech'}"

#example 9
my_info.clear()
print(my_info)
#---o/p---#
"{}"

#example 10
my_dict=('a','b','c','d')
print(dict.fromkeys(my_dict,0))
#---o/p---#
"{'a': 0, 'b': 0, 'c': 0, 'd': 0}"