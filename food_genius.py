import random
import warnings

"""
__"Hmm, what should I cook?"__
I.e. The Food Genius
A script which randomly chooses an item from a list and outputs it to the user
It will provide one of the items from Mains and sides, and a set meal as an alternative if desired over suggested 
It will also provide an idea for lunch 
Working progress being the lists' appendment 

TODO: 
    Make the list appendment work
        -> Consider using a JSON/XML file as a "Database" - makes it more dynamic and easier to append
    
    For dinner, suggest a combination of a main meal and a side, or a set meal 
        -> Consider creating a variable which combines both a side and main meal 
           and make it choose out of random from either a combo or a set meal 
        -> Combine set meal and combo sets together and make it randomly pick one 

    COME UP WITH MORE FOOD IDEAS (make the process easy too)
"""
lists = ["main.txt",        # list_id = 0
         "side.txt",        # list_id = 1
         "lunch.txt",       # list_id = 2
         "set_meals.txt"]   # list_id = 3


def home():

    """ Stands as a home function for the script
        This is the entry and exit point of the script """

    print("\nWhat would you like to do?:")
    print("1. Get food ideas")
    print("2. Add a new idea")
    print("3. Display all existing ideas")
    print("4. Exit")
    choice = input("Answer (number): ")

    if choice == "1":
        food_call()

    elif choice == "2":
        add_to_lists()

    elif choice == "3":
        display_lists()

    elif choice == "4":
        pass

    else:
        print("\nInvalid choice!")
        home()


def list_append(list_id, new_idea):

    with open("C:/Users/User/Desktop/The vicious Snake/Food Genius/" + lists[list_id], "a") as food_file:
        food_list = food_file.read().split(",")
        food_list.write(new_idea)


def food_list(list_id):

    with open("C:/Users/User/Desktop/The vicious Snake/Food Genius/" + lists[list_id], "r") as food_file:
        food_list = food_file.read().split(",")
        return food_list


def food_call():

    """ Providing a random item from each list and displaying it to the 
        user 
    """

    #Getting random items from lists
    random_main = random.choice(food_list(0))
    random_side = random.choice(food_list(1))
    random_lunch = random.choice(food_list(2))
    random_set_meal = random.choice(food_list(3))


    print("For dinner, you can have " + random_main + " with " + random_side)
    print("...or you could have " + random_set_meal)
    print("\nFor lunch tomorrow, you could have " + random_lunch)

    home()


def add_to_lists():
    """ Appending existing lists with new ideas 
        This is the function that made me realise why Python is kinda crap:
        NO SWITCH STATEMENTS!"""

    list_choice = input("Main/Side/Set Meal/Lunch?: ")
    
    if list_choice == "main":
        new_main_idea = input("New main meal idea: ")

        if new_main_idea == "":
            print("Nothing has been entered")
            new_main_idea = input("Try again?: ")
        
        elif new_main_idea in food_list(0):
            print("Idea already exists")
            new_main_idea = input("Try again?: ")
        else:
            list_append(0, new_main_idea)
            print("Your new main idea, " + new_main_idea + " was added to your list of Mains.")

    
    elif list_choice == "side":
        new_side_idea = input("New side idea: ")

        if new_side_idea == "":
            print("Nothing has been entered")
            new_side_idea = input("Try again?: ")

        elif new_side_idea in food_list(1):
            print("Idea already exists")
            new_side_idea = input("Try again?: ")

        else:
            list_append(1, new_side_idea)
            print("Your new side idea, " + new_side_idea + " has been added to your list.")

    

    elif list_choice == "set meal":
        new_set_meal_idea = input("New set meal idea: ")

        if new_set_meal_idea == "":
            print("Nothing has been entered.")
        
        elif new_set_meal_idea in food_list(3):
            print("Idea already exists")
            new_set_meal_idea = input("Try again?: ")
        else:
            list_append(3, new_set_meal_idea)
            print('Your new set meal idea, "%s" has been added to the list.' % new_set_meal_idea)


    
    elif list_choice == "lunch":
        new_lunch_idea = input("New lunch idea: ")

        if new_lunch_idea == "":
            print("Nothing has been entered")
            new_lunch_idea = input("Try again?: ")
        
        elif new_lunch_idea in food_list(2):
            print("Idea already exists")
            new_lunch_idea = input("Try again?: ")
        
        else:
            list_append(2, new_lunch_idea)
            print("Your new lunch idea, " + new_lunch_idea + ", is in the bag!")

    

    elif list_choice == "":
        print("\nK then.")

    else:
        print("Invalid choice!")
        add_to_lists()

    home()


def display_lists():

    """ Does what it says on the tin - displays the current lists
        Oh, and makes it look a bit nicer
        TODO: Get rid of those quotes somehow """

    main_list = food_list(0)
    side_list = food_list(1)
    set_meal_list = food_list(3)
    lunch_list = food_list(2)

    print("\nMain ideas: %s (Total: %s)" % (str(main_list), str(len(food_list(0))))
    
    home()
    
    
        
#Initiating introductory function
# home()