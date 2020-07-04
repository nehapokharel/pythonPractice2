friends_name = []

friends_name.append("John")
friends_name.append("Sara")
friends_name.append("Asmee")
friends_name.append("Keshav")
friends_name.append("Kamal")
friends_name.append("Kamala")

print(id(friends_name))

#On appending the new item, the id of list has changed.

friends_name.sort()
print("first item: " + friends_name[0])
print("second item: " + friends_name[1])
