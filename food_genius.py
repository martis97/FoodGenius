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
    For dinner, suggest a combination of a main meal and a side, or a set meal 
        -> Consider creating a variable which combines both a side and main meal 
           and make it choose out of random from either a combo or a set meal 
        -> Combine set meal and combo sets together and make it randomly pick one 

    COME UP WITH MORE FOOD IDEAS (make the process easy too)
"""


class FoodGenius:

    def __init__(self):
        self.lists = ["main.txt",        # list_id = 0
                      "side.txt",        # list_id = 1
                      "lunch.txt",       # list_id = 2
                      "set_meals.txt"]   # list_id = 3
    
    def __main__(self):
        self.home()

    def home(self):
        """ Stands as a home function for the app
            This is the entry and exit point of the script """
        
        while 1==1:
            print("\nWhat would you like to do?:")
            print("1. Get food ideas")
            print("2. Add a new idea")
            print("3. Display all existing ideas")
            print("4. Exit")
            choice = input("Answer (number): ")

            if choice == "1":
                self.food_call()

            elif choice == "2":
                self.add_to_lists()

            elif choice == "3":
                self.display_lists()

            elif choice == "4":
                break

            else:
                print("\nInvalid choice!")


    def list_append(self, list_id, new_idea):

        with open("C:/Users/User/Desktop/The vicious Snake/Food Genius/ideas/"  \
                + self.lists[list_id], "a") as food_file:

            food_list = food_file.read().split(",")
            food_list.write(new_idea)


    def food_list(self, list_id):

        with open("C:/Users/User/Desktop/The vicious Snake/Food Genius/ideas/" \
                + self.lists[list_id], "r") as food_file:
            
            food_list = food_file.read().split(",")
            return food_list


    def food_call(self):
        """Providing a random item from each list and displaying it to the 
        user 
        """

        #Getting random items from lists
        random_main = random.choice(self.food_list(0))
        random_side = random.choice(self.food_list(1))
        random_lunch = random.choice(self.food_list(2))
        random_set_meal = random.choice(self.food_list(3))


        print("For dinner, you can have %s with %s" % random_main, random_side)
        print("...or you could have %s" % random_set_meal)
        print("\nFor lunch tomorrow, you could have %s" % random_lunch)


    def add_to_lists(self):
        """Appending existing lists with new ideas 
        This is the function that made me realise why Python is kinda crap:
        NO SWITCH STATEMENTS!
        """

        list_choice = input("Main/Side/Set Meal/Lunch?: ")

        retry_limit = 3

        while 1==1:   
            if list_choice == "main":
                new_main_idea = input("New main meal idea: ")
                if new_main_idea == "":
                    print("Nothing has been entered")
                    new_main_idea = input("Try again?(Retries left: %d) : " % retry_limit)
                    retry_limit -= 1
                    if retry_limit == 0:
                        break
                elif new_main_idea in self.food_list(0):
                    print("Idea already exists")
                    new_main_idea = input("Try again?(Retries left: %d) : " % retry_limit)
                    retry_limit -= 1
                    if retry_limit == 0:
                        break
                else:
                    self.list_append(0, new_main_idea)
                    print("Your new main idea '%s' was added to your list of Mains." % new_main_idea)
            
            elif list_choice == "side":
                new_side_idea = input("New side idea: ")
                if new_side_idea == "":
                    print("Nothing has been entered")
                    new_side_idea = input("Try again?(Retries left: %d): " % retry_limit)
                    retry_limit -= 1
                    if retry_limit == 0:
                        break
                elif new_side_idea in self.food_list(1):
                    print("Idea already exists")
                    new_side_idea = input("Try again?(Retries left: %d): " % retry_limit)
                    retry_limit -= 1
                    if retry_limit == 0:
                        break
                else:
                    self.list_append(1, new_side_idea)
                    print("Your new side idea, '%s' has been added to your list." % new_side_idea)

            elif list_choice == "lunch":
                new_lunch_idea = input("New lunch idea: ")
                if new_lunch_idea == "":
                    print("Nothing has been entered")
                    new_lunch_idea = input("Try again? (Retries left: %d): " % retry_limit)
                    retry_limit -= 1
                    if retry_limit == 0:
                        break
                elif new_lunch_idea in self.food_list(2):
                    print("Idea already exists")
                    new_lunch_idea = input("Try again?(Retries left: %d): " % retry_limit)
                    retry_limit -= 1
                    if retry_limit == 0:
                        break
                else:
                    self.list_append(2, new_lunch_idea)
                    print("Your new lunch idea, '%s', is in the bag!" % new_lunch_idea)

            elif list_choice == "set meal":
                new_set_meal_idea = input("New set meal idea: ")
                if new_set_meal_idea == "":
                    print("Nothing has been entered.")
                elif new_set_meal_idea in self.food_list(3):
                    print("Idea already exists")
                    new_set_meal_idea = input("Try again?(Retries left: %d) : " % retry_limit)
                    retry_limit -= 1
                    if retry_limit == 0:
                        break
                else:
                    self.list_append(3, new_set_meal_idea)
                    print("Your new set meal idea, '%s' has been added to the list." % new_set_meal_idea)
            

            elif list_choice == "":
                print("\nNothing detected. Try again (Retries left: %d)" % retry_limit)
                retry_limit -= 1
                if retry_limit == 0:
                    break

            else:
                print("Invalid choice!")


    def display_lists(self):

        """ Does what it says on the tin - displays the current lists
            Oh, and makes it look a bit nicer
            # # # TODO: Fix and complete this """

        main_list = self.food_list(0)
        side_list = self.food_list(1)
        set_meal_list = self.food_list(3)
        lunch_list = self.food_list(2)

        print("\nMain ideas: %s (Total: %d)" % str(main_list), len(self.food_list(0)))