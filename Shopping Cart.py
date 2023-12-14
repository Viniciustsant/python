#I made some changes so the price appears next to the product name, aligning the prices
#I also added some time.sleep to make it more visual and easier to read


import time

#lists
itens = []
prices = []
#empty variable
menu_choice = ""
itens_count = len(itens)
#loop menu
while menu_choice.lower() != "5":
    print ("\n Please select one of the following: ")
    print ("\n 1. Add item \n 2. View cart \n 3. Remove item \n 4. Compute total \n 5. Quit ")
    menu_choice = input ("\n Please enter an action: ")

#first option    
    if menu_choice == "1":
        time.sleep (1)
        adding_item = input (" \n What item would you like to add?  ")
        price_item = float(input (f" What is the price of '{adding_item}'? "))
        time.sleep (2)
        print (f" ' {adding_item}' has been added to the cart. ")
        time.sleep (2)
        #adding to the list
        itens.append (adding_item)
        prices.append (price_item)
        #updating the len of the list
        itens_count += 1

#second option
    elif menu_choice == "2":
        time.sleep(2)
        print (" The contents of the shopping cart are: ")
        for i in range (len (itens)):
            print (f"{i + 1}. {itens[i]} - $ {prices[i]:.2f}")
        time.sleep(2)

#third option
    elif menu_choice == "3":
        time.sleep (2)
        removing = int(input (" Which item would you like to remove?  "))
        #checking if the enter is valid
        while removing > itens_count or removing <= 0 :
            print (" Please enter a valid number! ")
            time.sleep (1)
            removing = int(input (" Which item would you like to remove?  "))

        else:
            #removing from the list
            itens.pop (removing - 1)
            prices.pop (removing - 1)
            time.sleep (1)
            print (" Item removed. ")
            #updating the len of the list
            itens_count -= 1
            time.sleep(2)

# fourth option 
    elif menu_choice == "4":
        total = sum(prices)
        time.sleep(2)
        print (f" The total price of the items in the shopping cart is $ {total:.2f}")
        time.sleep(2)

#final
time.sleep (1)
print (" \n Thank you. Goodbye. ")
        