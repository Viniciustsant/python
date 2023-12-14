#Adventure game
#I added a few more parts to the story, and put a little more than four questions in one part to make the game have a little more emotion.
#there are a comments in each place, indetifying each question and process

print('\nWelcome to the greatest adventure of all time! \n')

#firt part of the story
print('Imagine that you are on a boat in the Caribbean islands, and without realizing it you were carried by')
print('the tide into a strong current that is taking you away from your island  ')
first_choice= input('You have two options, try to PADDLE against the current or SCREAM for help, which do you choose?  ')
#if the answer choose paddle
if first_choice.lower() == 'paddle':
    print('\nYou managed to get out of the current with a lot of effort, but when you realized, that effort ended up ')
    print('puncturing the boat where you are, You need to think quickly to save yourself,  ')
    #second question
    first_paddle_choice= input('Do you JUMP into the water and try to swim to the island, look for something to try to REPAIR the boat or ROW to try to get to the island before the boat sinks?  ')
    if first_paddle_choice.lower () == 'jump':
        #third question
        last_choice_paddle= input('You started to swim, but when you looked down you saw a shark approaching you, do you want to RUN AWAY from the shark or FIGHT with it? ')
        if last_choice_paddle.lower == 'run away':
            #final
            print("Rest in peace, you were tired after jumping into the water and swimming a lot, you felt cramps and became a shark snack! ")
        elif last_choice_paddle.lower() == 'fight':
            print("The fight was arduous, but you were brave, you lost an arm and part of your left leg, but you managed to get rid of it and get to the shore and survive, congratulations, you are a warrior!")
        else:
            print('Type one of the options presented in capital letters')
    elif first_paddle_choice.lower() == 'repair':
        #third question
        last_choice_repair= input("You found some WOOD GLUE and an OLD SHIRT, which one do you choose to repair the boat?")
        if last_choice_repair.lower() == 'wood glue':
            #final
            print("Rest in peace, the water was coming in too quickly, the glue wasn't able to solve the problem, and you became shark food! ")
        elif last_choice_repair.lower() == 'old shirt':
            print("You did well, the shirt stopped the water from entering until your family missed you and rescued you with another boat, be careful next time! ")
        else:
            print('Type one of the options presented in capital letters')
    elif first_paddle_choice.lower() == 'row':
        #third question
        last_choice_row= input ('Your boat is sinking more and more, KEEP paddling or JUMP out?  ')
        if last_choice_row.lower() == 'keep':
            #final
            print("Rest in peace, you sank before reaching the island and you no longer had the strength to swim, you became shark food! ")
        elif last_choice_row.lower() == 'jump':
            print("Rest in peace, all the commotion in the water attracted sharks, and you became their snack! ")
        else:
            print('Type one of the options presented in capital letters')
    else:
        print('Type one of the options presented in capital letters')
#if choose scream
elif first_choice.lower() == 'scream':
    print('You were very far from the island and no one heard you, now you have been carried away by the current for about an hour and are in the open sea with no sight of land nearby. ')
    #second question
    first_scream_choice= input("You're lost, what are you going to do? try to PADDLE through the current and return to where you were, LOOK for another island or WAIT for someone to look for you?   ")
    if first_scream_choice.lower() == 'paddle':
        #third question
        last_choice_paddle_1 =input("Complicated choice, the current is very strong and broke your oar, now you only have two options, WAIT for rescue or jump into the water and SWIM, which do you choose?  ")
        if last_choice_paddle_1.lower() == 'wait':
            #final
            print("Rest in peace, the current made it impossible for the rescue team to find you and you died of hunger and thirst! ")
        elif last_choice_paddle_1.lower() == 'swim':
            print('Never swim in a strong current, you will drown, rest in peace! ')
        else:
            print('Type one of the options presented in capital letters')
    elif first_scream_choice.lower() == 'look':
        #third question
        last_choice_look= input("You saw an island far away from you and managed to get to it, it's getting dark and you're hungry, are you going to HUNT something to eat, build a TENT or make a SIGN so rescuers can find you?  ")
        if last_choice_look.lower() == 'hunt':
            #forth question
            choice_hunt= input("You got some fruits and fish, good hunting, now it's time to rest, but you don't have a tent, are you going to sleep under a TREE or inside a CAVE?  ")
            if choice_hunt.lower() == 'tree':
                #final
                print ("The nights on the island are very cold, it rained and you ended up getting sick and without being able to protect yourself or get water or food, you ended up dying! ")
            elif choice_hunt.lower() == 'cave':
                print("Caves on desert islands are very dangerous, a poisonous snake bit you while you were sleeping and you died! ")
            else:
               print('Type one of the options presented in capital letters')
        elif last_choice_look.lower() == 'tent':
            #forth question
            choice_tent= input("Good choice, the nights on the island are very cold, you built a tent fortified against rain and predators, but you are very hungry, are you going to LOOK for food late at night or SLEEP and look for something in the morning?  ") 
            if choice_tent.lower() == 'look':
                #final
                print("Predators also hunt at night, you ended up becoming food, rest in peace! ")
            elif choice_tent.lower() == 'sleep':
                print("Good choice, you felt quite hungry at night, but you survived, in the morning you ate some fish and drank coconut water and the rescue found you, congratulations! ")
            else:
                print('Type one of the options presented in capital letters')
        elif last_choice_look.lower() == 'sign':
            print("You made a beautiful sign, but it was late and you were hungry, cold and without protection, you were easy prey for the island's predators, rest in peace! ")
    elif first_scream_choice.lower() == 'wait':
        #third question
        
        else:
           print('Type one of the options presented in capital letters') 
else:
    print('Type one of the options presented in capital letters')