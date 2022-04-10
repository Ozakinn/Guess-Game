#Guess Game - Krystler Cataniag
import os #for Clearning Windows CMD
import time #Add delays

global_difficulty = 0 #Game Difficulty. DO NOT MODIFY.

def game_engine():
    global global_difficulty
    
    
    whitespace = "   "
    box = "\U0001F381"
    
    player_pov = "          "
    
    while global_difficulty != 0:
        player_pov = player_pov+box+whitespace
        global_difficulty-=1
    
    print("")
    print(player_pov)
    print("")
        
    

def game_start():
    
    #Clear TERMINAL for WINDOWS
    os.system("cls")
    
    countdown = 3
    while countdown <= 4:
        print("")
        print("          Game Start in ",countdown,"...")
        time.sleep(1)
        countdown-=1
        #Clear TERMINAL for WINDOWS
        os.system("cls")
        
        if countdown == 0:
            game_engine()
            break
            
        
    

def menu():
    menuCheck = 0
    #Clear TERMINAL for WINDOWS
    os.system("cls")
    
    #global variable to be use based on difficulty
    global global_difficulty
    
    while menuCheck == 0:
    
        print("")
        print("          \U0001F381GUESS GAME\U0001F381          ")
        print("         Krystler Cataniag          ")
        print("")
        print("          (1) \U0001F476Easy")
        print("          (2) \U0001F468Average")
        print("          (3) \U0001F9B8Hard")
        print("")
        menu_Select = input("Select Difficulty: ")
        
        
        try:
            menuSelectCheck = int(menu_Select)
            
            if menuSelectCheck == 1:
                menuCheck = 1
                
                #Clear TERMINAL for WINDOWS
                os.system("cls")
                
                 #remind what the user selected
                print("")
                print("            You've Selected")
                print("                 \U0001F476Easy")
                print("")
                time.sleep(2) #wait for 2 secs
                
                global_difficulty = 2
                
                game_start()
            
            elif menuSelectCheck == 2:
                menuCheck = 1
                
                #Clear TERMINAL for WINDOWS
                os.system("cls")
                
                #remind what the user selected
                print("")
                print("            You've Selected")
                print("               \U0001F468Average")
                print("")
                time.sleep(2) #wait for 2 secs
                
                global_difficulty = 3
                
                game_start()
                
            elif menuSelectCheck == 3:
                menuCheck = 1
                
                #Clear TERMINAL for WINDOWS
                os.system("cls")
                
                #remind what the user selected
                print("")
                print("            You've Selected")
                print("                 \U0001F9B8Hard")
                print("")
                time.sleep(2) #wait for 2 secs
                
                global_difficulty = 4
                
                game_start()
                
        except:
            #continue to ask difficulty until the user enter correct value.
            menuCheck = 0
            print("")
            print("Plese enter numbers only based on difficulty.")
            time.sleep(2)

    
menu()