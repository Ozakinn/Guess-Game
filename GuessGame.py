#Guess Game - Krystler Cataniag
import os #for Clearing Windows CMD
import time #Add delays
import random #random value of hidden object during gameplay

global_difficulty = 0 #Game Difficulty. DO NOT MODIFY.
global_emoji = "0" #hidden item emoji based on difficulty. DO NOT MODIFY.
global_hdn_item = 0 #Value of hidden item to be accesible to other functions(def) DO NOT MODIFY
global_HP = 0 #Value of player Health will base on chosen difficulty. DO NOT MODIFY
global_score = 0 #Value of player Score for correct answers. DO NOT MODIFY

#declare and initialize the game pov or the answer key
global_game_pov = ""
global_game_pov_num = ""

#this function calculates and generates the difficulty and emojis
def game_engine():
    
    #declaring the global to be access here in this function
    global global_difficulty, global_emoji, global_hdn_item, global_HP, global_score, global_game_pov, global_game_pov_num
    
    #Continiously run the guess game until no Health left
    while global_HP != 0:
        
        #Clear TERMINAL for WINDOWS
        os.system("cls")
        
        #declare and initialize seperate difficulty for easy understanding.
        game_difficulty = global_difficulty
        player_difficulty = global_difficulty
        
        #Calculate player HP and generate heart Emoji
        player_HP = global_HP
        player_HP_emoji = "\U0001F496"
        player_HP_pov = "          "
        z_loop = 1
        while z_loop <= player_HP:
            player_HP_pov = player_HP_pov + player_HP_emoji
            z_loop+=1
        
        #Generate the value of hidden emoji and prefixes
        whitespace = "   "
        box = "\U0001F381"
        global_hdn_item = random.randint(1, global_difficulty)
        
        #Player point of view
        #Item is hidden
        #Generate the guess game boxes.
        player_pov = "          "
        player_pov_boxnum = "          "
        x_loop = 1
        while x_loop <= player_difficulty:
            player_pov = player_pov + box + whitespace
            player_pov_boxnum = player_pov_boxnum + " "+str(x_loop) + whitespace
            x_loop+=1
        
        #Game point of view
        #item is visible
        #Generate the guess game boxes with showned hidden emoji.
        global_game_pov = "          "
        global_game_pov_num = "          "
        itemCheck = ""
        y_loop = 1
        while y_loop <= game_difficulty:
            
            #match the loop with the current random value of hidden object.
            #this is to match the number of emoji when displayed.
            if y_loop == global_hdn_item:
                itemCheck = global_emoji #the hidden emoji
            else:
                itemCheck = "\U0001F381" #box emoji
            
            global_game_pov = global_game_pov + itemCheck + whitespace
            global_game_pov_num = global_game_pov_num + " "+str(y_loop) + whitespace
            y_loop+=1
        
        #Display the SCORE, HEALTH
        print("")
        print("               Score: "+str(global_score))
        print(player_HP_pov +" | "+ str(player_HP) +" Health Left")
        
        #Display the player's point of view(the emoji is hiding)
        print("")
        print(player_pov)
        print(player_pov_boxnum)
        print("")
        
        #THIS IS FOR DEBUG PURPOSE
        #Allows you to see the answer/emoji during the guess process
        #print("")
        #print(global_game_pov)
        #print(global_game_pov_num)
        #print("")
        
        #Ask for user input
        user_answer()

#this function tells the result of the user's guessed number
def result(asnwered):
    
    #declaring the global to be access here in this function
    global global_difficulty, global_hdn_item, global_HP, global_score, global_game_pov, global_game_pov_num
    
    #Clear TERMINAL for WINDOWS
    os.system("cls")
    
    #Check if user answer is correct
    if global_hdn_item == asnwered:
        
        #add the score
        global_score+=1
        
        #display the answer or show the hidden emoji
        print("")
        print("")
        print("")
        print("")
        print(global_game_pov)
        print(global_game_pov_num)
        print("")
        
        #add HEALTH when correctly gueesing the emoji 2 times.
        if global_score % 2 == 0:
            global_HP+=1
            print("     +1 \U0001F496 | Correct \U00002705 | Score: "+str(global_score))
            print("")
        
        #display to user that the answer is correct
        else:
            print("          Correct \U00002705 | Score: "+str(global_score))
            print("")
        
        #wait for 3 seconds to loop again. back to guessing new boxes.
        time.sleep(3)
        
    #check if user answer is incorrect
    elif global_hdn_item != asnwered:
        
        #deduct player HEALTH
        global_HP-=1
        
        #display answer or emoji and the result of user answer
        print("")
        print("")
        print("")
        print("")
        print(global_game_pov)
        print(global_game_pov_num)
        print("")
        print("     -1 \U0001F494 | Incorrect \U0000274C | Score: "+str(global_score))
        print("")
        
        #display end game if player HP is ZERO(0)
        if global_HP == 0:
            print("                Guess what?")
            print("          You're out of \U0001F494 Health")
            print("")
            
        #wait for 3 seconds to loop again. back to guessing new boxes.
        time.sleep(3)
        
#this function ask for user's answer
def user_answer():
    
    #get the global value
    global global_difficulty
    
    #loop value to loop it again untill correct user input
    u_answercheck = 0
    
    #start of looping for correct input only.
    while u_answercheck == 0:
        
        #ask for user input
        print("Select box from 1 to "+str(global_difficulty))
        guess_Answer = input("Which box you want to guess? Select: ")
        
        #catch error when inputed answer is not valid or out of range.
        try:
            #convert to int, because we onl accept number for user input.
            guess_AnswerCheck = int(guess_Answer)
            
            #if user answer is a number and within the given box range.
            if guess_AnswerCheck <= global_difficulty:
                u_answercheck = 1 #this hould stop the loop
                result(guess_AnswerCheck) #Go to result function with parameter of the users answer
            else:
                #continue to loop if given boxes is out of range
                u_answercheck = 0
                
            
        except:
            #if there is an error converting to int or other error, this should catch it and continue the game.
            u_answercheck = 0
            print("")
            print("Plese enter numbers only based boxes.")
            time.sleep(2)
        

def game_start():
    
    global global_emoji, global_HP
    
    #Clear TERMINAL for WINDOWS
    os.system("cls")
    
    print("")
    print("      Find and Guess where this emoji hides "+global_emoji)
    print("        you only have "+str(global_HP)+ "\U0001F496 (Health) to try.")
    print("     +1 \U0001F496 after 2x correctly guessing the emoji.")
    time.sleep(3)
    
    countdown = 3
    while countdown <= 4:
        #Clear TERMINAL for WINDOWS
        os.system("cls")
        print("")
        print("      Find and Guess where this emoji hides "+global_emoji)
        print("        you only have "+str(global_HP)+ "\U0001F496 (Health) to try.")
        print("     +1 \U0001F496 after 2x correctly guessing the emoji.")
        print("               Game Start in ",countdown,"...")
        time.sleep(1)
        countdown-=1
        #Clear TERMINAL for WINDOWS
        os.system("cls")
        
        if countdown == 0:
            game_engine()
            break
            
        
#this function is for main menu, ask for difficulty selection
def menu():
    
    #declare and initialize the loop value.
    menuCheck = 0
    
    
    #global variable to be use based b all functions(difficulty, emoji , HP) 
    global global_difficulty, global_emoji, global_HP
    
    #start looping until the user input is correct and valid
    while menuCheck == 0:
        
        #Clear TERMINAL for WINDOWS
        os.system("cls")
        
        #display difficulty selection
        print("")
        print("          \U0001F381 GUESS GAME \U0001F381          ")
        print("          Krystler Cataniag          ")
        print("")
        print("          (1) \U0001F476 Easy")
        print("          (2) \U0001F468 Average")
        print("          (3) \U0001F9B8 Hard")
        print("")
        menu_Select = input("Select Difficulty: ")
        
        #This will catch user's incorrect input or invalid input
        try:
            #convert to int, the game expect a number
            menuSelectCheck = int(menu_Select)
            
            #if user inputed number is 1 or easy
            if menuSelectCheck == 1:
                menuCheck = 1 #this should stop the loop
                
                #Clear TERMINAL for WINDOWS
                os.system("cls")
                
                #remind what the user selected
                print("")
                print("            You've Selected")
                print("               \U0001F476 Easy")
                print("")
                time.sleep(2) #wait for 2 secs
                
                #add value to global variables
                global_difficulty = 2 #2 boxes
                global_emoji = "\U0001F476" #the hidden emoji
                global_HP = 10 #player Health
                
                #start initializing the game
                game_start()
            
            #if user inputed number is 2 or average
            elif menuSelectCheck == 2:
                menuCheck = 1 #this should stop the loop
                
                #Clear TERMINAL for WINDOWS
                os.system("cls")
                
                #remind what the user selected
                print("")
                print("            You've Selected")
                print("             \U0001F468 Average")
                print("")
                time.sleep(2) #wait for 2 secs
                
                #add value to global variables
                global_difficulty = 3 #3 boxes
                global_emoji = "\U0001F468" #the hidden emoji
                global_HP = 5 #player HP
                
                #start initializing the game
                game_start()
            
            #if user inputed number is 3 or hard
            elif menuSelectCheck == 3:
                menuCheck = 1 #this should stop the loop
                
                #Clear TERMINAL for WINDOWS
                os.system("cls")
                
                #remind what the user selected
                print("")
                print("            You've Selected")
                print("               \U0001F9B8 Hard")
                print("")
                time.sleep(2) #wait for 2 secs
                
                #add value to global variables
                global_difficulty = 4 #3 boxes
                global_emoji = "\U0001F9B8" #the hidden emoji
                global_HP = 3 #player HP
                
                #start initializing the game
                game_start()
            
            else:
                #continue to run the loop until the inputed number when out of range
                menuCheck = 0
                print("")
                print("Plese enter numbers only based on difficulty.")
                time.sleep(2)
                
        except:
            #continue to ask difficulty until the user enter correct value.
            menuCheck = 0
            print("")
            print("Plese enter numbers only based on difficulty.")
            time.sleep(2)

#run the whole code or this project
menu()