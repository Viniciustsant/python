#I added a time sleep to make the code cleaner 
#and a check so that if the user input does not contain any data, the message appears instead of the code failing

import time

#enter values
highest_expectation = 0
lowest_expectation = 100.000
highest_expectation_user = 0
lowest_expectation_user = 100.000
average_year = 0
count = 0

#verify if the enter is valid
while True:
    user_year = input ("Enter the year of interest (4 Digits): ")



    if user_year.isdigit() and len(user_year) == 4:
        user_year = int(user_year)
        break
    else:
        print("Please enter a valid 4-digits year. ")

#open file
with open ("life-expectancy.csv") as the_list:
    next(the_list)
    for item in the_list:

        #split list        
        parts = item.split(",")

        #definy itens in list
        country = parts[0]
        year = int(parts[2])
        life = float(parts[3])

#add the years of user input
        if year == user_year:
            average_year += life
            count += 1

        #Calculate lowest expectation
        if life < lowest_expectation:
            lowest_expectation = life
            lowest_country = country
            lowest_year = year

        #Calculate highest expectation       
        if life > highest_expectation:
            highest_expectation = life
            highest_country = country
            highest_year = year

        #Calculate the lowest expectation of user enter
        if int(year) == user_year:
            if life < lowest_expectation_user:
                lowest_expectation_user = life
                lowest_country_user = country 
                    
            #Calculate highest expectation for user enter
            if life > highest_expectation_user:
                highest_expectation_user = life
                highest_country_user = country

#verify if the year of the user enter is on the data
    if count > 0:
        average_expectation = average_year / count
    else:
        average_expectation = 0 

time.sleep(2)

#prints
print ()
print (f"The overall max life expectancy is: {highest_expectation} from {highest_country} in {highest_year}")
time.sleep (1)
print (f"The overall min life expectancy is: {lowest_expectation} from {lowest_country} in {lowest_year}")
time.sleep(3)
print()
print (f"For the year {user_year}: ")
time.sleep(1)

#verify if has any data of the year enter to show
if count > 0:
    print (f"The average life expectancy across all countries was {average_expectation:.2f}")
    time.sleep(1)
    print (f"The max life expectancy was in {highest_country_user} with {highest_expectation_user}")
    time.sleep(1)
    print (f"The min life expectancy was in {lowest_country_user} with {lowest_expectation_user}")
else:
    print ("No data found for this year")
print()
        