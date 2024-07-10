list1 = [1,"This is list 1",3.5]
list2 = [True, "This is list 2", False]

list1.extend(list2)
print(list1)

#Built in Functions

#Add an item
list1.append('A New Item')
print(list1)

#Copy the list
result = list1.copy()
print(result)

#Remove any item
list1.remove('A New Item')
print(list1)

#Remove last item
result=list1.pop()
print(list1)
print(result)

#Sort itmes
list_names = ["Anna", "Kevin", "Stephen", "Daniel", "Adam", "Joe", "Maria", "Adele"]
list_names.sort()
print(list_names)

list_num = [34,6,56,44,87,0,-23,100]
list_num.sort()
print(list_num)