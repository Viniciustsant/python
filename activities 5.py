#names_of_friends = []

#name_input = ""
#while name_input.lower() != "end":
#    name_input = input ("Type the name of a friend:  ")
#    if name_input.lower() != "end":
#        names_of_friends.append (name_input)
#print ("Your friends are: ")
#for name in names_of_friends:
#    print (name)

# activity 2
shopping_lists = []

shopping_itens = ""

while shopping_itens.lower() != "end":
    shopping_itens = input (" Please enter the itens of the shopping list (type: quit to finish): ")
    if shopping_itens. lower () != "end":
        shopping_lists.append (shopping_itens)
print ("\nThe shopping list is:")
for item in shopping_lists :
    print (item)
print ("\nThe shopping list with indexes is:")
for i in range (len (shopping_lists)):
    print (f"{i}. {shopping_lists[i]}")

#trocar item
index_number = int ( input ("\nWhich item would you like to change?  "))
new_item = input ("\nWhat is the new item?  ")
shopping_lists[index_number] = new_item
print ("\nThe shopping list with indexes is:")
for i in range (len (shopping_lists)):
    print (f"{i}. {shopping_lists[i]}")