#age= int(input ('how old are you?  ')) 
#birthday= age + 1
#text= f'On your next birthday, you will be {birthday} '
#print (text)

#eggs_cartons= int(input('How many egg cartons do you have?  '))
#calculate= eggs_cartons * 12
#total= f'You have {calculate} eggs'
#print(total)

#cookies= int(input('\nhow many cookies do you have?  '))
#people= int(input ('how many people are there?  '))
#division= cookies/ people
#result= f'Each person may have {division} cookies'
#print (result)

#favorite color
#favorite_color= input('\nPlease enter yout favorite color:  \n')
#favorite_color_adapted= str(favorite_color)
#print('Your favorite color is'+''+ favorite_color)

#numero_um = int(input('\nDigite um número inteiro: '))
#numero_dois = int(input('Digite um segundo número inteiro: '))
#if numero_um > numero_dois:
#    print ('O primeiro número é maior ')
#else :
#    print('O primeiro número não é maior ')

#if numero_um == numero_dois:
#    print('Os números são iguais ')
#else :
#    print('Os números não são iguais ')
#if numero_dois> numero_um:
#    print('O segundo número é maior ')
#else:
#    print('O segundo número não é maior ')

#favorite_animal = input ('\nQual é seu animal favorito?  ')
#if favorite_animal.lower() == 'cachorro' :
#    print ('Esse também é meu animal favorito! ')
#else:
#    print('Esse não é meu animal favorito! ')

#gpa= float(input('What was your Grade Point Average?  ')) 
#lowest_grade= float(input('What was you lowest grade?  '))
#if gpa>= .85:
    #if lowest_grade>= .70: 
        #print('You made the honour roll! ')

#loan money
#print ('\nRate from 1-10 the following: \n')
#loan= int(input('How large is the loan?  '))
#credit= int(input('How good is your credit history?  '))
#income= int(input('How high is your income?  '))
#payment= int(input('How large is your down payment?  '))
#should_loan= False

#if loan>= 5:
#    if credit >= 7 and income>= 7:
#        should_loan= True
#    elif credit >= 7 or income >= 7 :
#        if payment>= 5:
#            should_loan= True
#        else:
#            should_loan= False
#    else:
#        should_loan=False
#else: 
#    if credit<4:
#        should_loan= False
#    else:
#        if income>= 7 or payment>= 7:
#            should_loan= True
#        elif income>=4 and payment>= 4:
#            should_loan= True
#        else:
#            should_loan=False
#if should_loan:
#    print('\nThe decision is yes. This is a good loan. ')
#else:
#    print('The decision is no. You should not loan this money.')
#elif first_choice.lower() == 'scream':
    #print('You were very far from the island and no one heard you, now you have been carried away by the current for about an hour and are in the open sea with no sight of land nearby.')
    #first_scream_choice= input('')

#loops
#number= int(input("\nWrite a number: \n"))
#while number < 0:
#        print("Please, enter positive numbers only ")
#        number= int(input("Write a number: \n"))
#print(number)

#question= input("\nMay i have a piece of candy?  \n")
#while question == 'no':
#or
#while question != 'yes':
#    question= input("\nMay i have a piece of candy?  \n")
#print("Thank you! S2 ")
#import time
#for
#time.sleep(2)
#colors = ["\nred", "blue", "green", "yellow"]
#for color in colors:
#    print (color)
#print()

#time.sleep(2)
#for i in range(1, 9):
#    print(i)
#print()

#time.sleep(2)
#for i in range(2,22,2):
#    print (i)

#file_path = "C:/Users/Usuario/Onedrive/Área de Trabalho/Projetos/books.txt"
#with open (file_path, 'r', encoding='utf-8') as book_mormon:
#with open ("books.txt") as book_mormon:
#    for line in book_mormon:
#        clean_line = line.strip()
#        print (f"{clean_line}")

#people = [
#    "Stephanie 36",
#    "John 29",
#    "Emily 24",
#    "Gretchen 54",
#    "Noah 12",
#    "Penelope 32",
#    "Michael 2",
#    "Jacob 10"
#]


#for person in people:
#    print (person)

#people_splited = [person.split() for person in people]
#print (people_splited[0])
#print (people_splited[1])

def display_regular (message):
    print (message)

def display_uppercase (message):
    upper_message = message.upper()
    print(upper_message)

def display_lowercase (message):
    lower_message = message.lower()
    print(lower_message)

user_phrase = input("What  is your message? ")

display_lowercase (user_phrase)
display_regular (user_phrase)
display_uppercase(user_phrase)