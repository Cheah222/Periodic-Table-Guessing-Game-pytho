"""to import random library"""
import random
"""to generate random number"""
num=random.randint(1,10)
"""make the guess variable to null"""
guess = None
"""execute a set of statements as long as a condition is true"""
while guess !=num:
    """integer only for whole numbers"""    
    guess = int(input("Guess a number between 1 to 10: "))
    """to detect whether the statement is true or not"""    
    if guess < num:
        print ("too low")
    elif guess > num:
        print ("too high")
        """if guess correct, then else"""        
    else:
        print("You found the periodic number!")
        if guess == 1:
            print ("H")
        elif guess == 2:
            print ("He")
        elif guess == 3:
            print ("Li")
        elif guess == 4:
            print ("Be")
        elif guess == 5:
            print ("C")
        elif guess == 6:
            print ("N")
        elif guess == 7:
            print ("O")
        elif guess == 8:
            print ("Ne")
        elif guess == 9:
            print ("Na")
        elif guess == 10:
            print ("Mg")

        """string only for words"""
        x = str(input("What is the full name of this symbol? "))
        if x == "Hydrogen":       
            print ("Yes,you're right!")
            print ("Thanks for answering, have a nice day :)")
        elif x == "Helium":
            print ("Yes,you're right!")
            print ("Thanks for answering, have a nice day :)")
        elif x == "Lithium":
            print ("Yes,you're right!")
            print ("Thanks for answering, have a nice day :)")
        elif x == "Beryllium":
            print ("Yes,you're right!")
            print ("Thanks for answering, have a nice day :)")
        elif x == "Carbon":
            print ("Yes,you're right!")
            print ("Thanks for answering, have a nice day :)")
        elif x == "Nitrogen":
            print ("Yes,you're right!")
            print ("Thanks for answering, have a nice day :)")
        elif x == "Oxygen":
            print ("Yes,you're right!")
            print ("Thanks for answering, have a nice day :)")
        elif x == "Neon":
            print ("Yes,you're right!")
            print ("Thanks for answering, have a nice day :)")
        elif x == "Sodium":
            print ("Yes,you're right!")
            print ("Thanks for answering, have a nice day :)")
        elif x == "Magnesium":
            print ("Yes,you're right")
            print ("Thanks for answering, have a nice day :)")
                        
            
    
    
            
            
