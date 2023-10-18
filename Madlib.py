"""
Title: MadLib
Author: Makayla Wray
Date: 09-03-2023

Description:A Mad Libs Python program that is a fun and interactive game
that allows users to create humorous and often absurd stories by
inputing words of their choice. 

"""
def main():
    
    welcome()
    mad_lib()
    play_again()

def welcome():
    """This function generates a Welcome Message for the User"""

    print("Thank you for interacting with my Madlib. Please enjoy!")
    print()
    print("In this game, you'll be asked to provide various words such as nouns, verbs, adjectives, and places")
    print("to complete a fun and creative letter to your mom.Your inputs will be used to fill in the blanks in the story,")
    print("resulting in a hilarious and unique tale.")
    print()
    print("Follow these steps to play:")
    print()
    print("You will be asked to input multiple adjectives, nouns, verbs, and numbers.")
    print("Type your word and press Enter to submit your input. The program will prompt you for the next word.")
    print("You can be as creative or as silly as you want with your word choices!")
    print("Once you've filled in all the blanks, the completed Mad Libs story will be revealed to you.")
    print("Get ready to laugh at the wacky and unexpected narrative you've created!")



def mad_lib():
    """ This function takes the users inputs and insert it into the MadLib prompt"""

    print()

    adjective1 = input("Type your adjective 1:")
    adjective2 = input("Type your adjective 2:")
    adjective3 = input("Type your adjective 3:")
    adjective4 = input("Type your adjective 4:")
    adjective5 = input("Type your adjective 5:")
    adjective6 = input("Type your adjective 6:")

    print()

    fav_subject = input("Type your favorite subject:")

    print()

    occupation = input("Type your favorite ocupation:")

    print()

    number1 = int(input("Type a number between 0-100:"))

    while number1 not in range(0,101):
        print("Invalid Number, please try again")
        number1 = int(input("Type a number between 0-100:"))

    number2 = int(input("Type a number between 0-10000000: "))

    while number2 not in range(0,10000000):
        print("Invalid Number please try again")
        number2 = int(input("Type a number between 0-10000000: "))

    print()

    verb1 = input("Type a present tense verb with no \'-ING\' ending:")
    verb2 = input("Type a present tense verb with an \'-ING\' ending:")

    print()

    day_of_week = input("Type a day of the week:")

    print()

    food1 = input("Type your food 1 (plural):")
    food2 = input("Type your food 2(singular): ")
    food_place = input("Type your favorite restaurant:")

    print()

    object = input("Type a noun in plural tense:")

    print()

    item = input("Type a noun in singular tense:")

    print()

    madlibs = f"""Dear mom, I want you to know that your {adjective1} child is doing {adjective2} in \n
    school. So far, I have passed all my exams in my {fav_subject} class! After everything I learned so \n
    far, I feel like I am more prepared to become a(n) {occupation}. I've made {number1} friends and planning on \n
    making more {adjective3}, friends next semester. My friends and I have alot in common and like to \n
    {verb1} on {day_of_week} whenever we are not {verb2}. The food here is {adjective5} but sometimes I \n
    like to buy {food1} at {food_place}. I may be running low on {object}. Could you and dad send me {number2} \n
    dollars please. I miss being home and eating your {food2}. I can't wait to come home and give you a warm \n
    {item}!"""

    print(madlibs)

    
def play_again():
    """This function allows the user to choose if they want to play again or not"""
    again = input("Do you want to play again (y or n)")
    while again != "y" and again != "n":
        print("I'm sorry. I do not understand that response. Please try again")
        again = input("Do you want to play again (y or n)")
        if again == "y":
            mad_lib()
            play_again()
        elif again == "n":
            print("Okay, thank you for playing")
            break   

main()
      
      
 
