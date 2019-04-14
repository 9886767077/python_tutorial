fruits_list = ["apple", "mango", "banana", "orange", "mango", "mango", "papaya"]

fruits_list.insert(1,"kiwi")
fruits_list.append("guava")
fruits_list.extend(["grapes", "butter fruit", "peach"])
print(fruits_list)

ind = fruits_list.index("orange")
print ("index of orange is {}".format(ind))

fruits_list.remove("papaya")
print(fruits_list)

last_element = fruits_list.pop()
print("last element of the list is : {}".format(last_element))





