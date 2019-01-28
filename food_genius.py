import random
import warnings

"""
__"Hmm, what should I cook?"__
I.e. The Food Genius
A script which randomly chooses an item from a list and outputs it to the user
It will provide one of the items from Mains and Sides, and a set meal as an alternative if desired over suggested 
It will also provide an idea for lunch

TODO: 
    -> Split some functions to different classes:
        # List definition and actions upon it: class FoodStore 
                                                    ....start involving ingredients?.
        # Keep the rest to this class as it is and improve it.
    
"""


class FoodGenius:

    def __init__(self):
        self.meals = [("main","main.txt", 0), \
                      ("side", "side.txt", 1), \
                      ("lunch", "lunch.txt", 2), \
                      ("set meal", "set_meals.txt", 3)]
        main_list = self.food_list(0)
        side_list = self.food_list(1)
        set_meal_list = self.food_list(3)
        lunch_list = self.food_list(2)
    
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
                self.add_to_ideas()

            elif choice == "3":
                self.display_ideas()

            elif choice == "4":
                break

            else:
                print("\nInvalid choice!")


    def list_append(self, list_id, new_idea):
        """Read and append a selected list given its ID."""

        with open("C:/Food Genius/ideas/" + self.ideas[list_id], "a")  \
            as food_file:

            food_list = food_file.read().split(",")
            food_list.write(new_idea)


    def food_list(self, list_id):
        """Read and return a selected list given its ID.
        
        Returns:
            food_list = (list) All entries in the file returned in a list.
        """

        with open \
            (f"C:/Users/User/Desktop/The vicious Snake/Food Genius/ideas/\{self.ideas[list_id]}" \
            , "r") as food_file:
            
            food_list = food_file.read().split(",")
            return food_list


    def food_call(self):
        """Providing a random item from each list and displaying it to the 
        user 
        """

        #Getting random items from ideas
        random_main = random.choice(self.food_list(0))
        random_side = random.choice(self.food_list(1))
        random_lunch = random.choice(self.food_list(2))
        random_set_meal = random.choice(self.food_list(3))


        print(f"For dinner, you can have {random_main} with {random_side}")
        print(f"...or you could have {random_set_meal}")
        print(f"\nFor lunch tomorrow, you could have {random_lunch}")
    
    def add_to_list(self, idea_type):
        retry_limit = 2
        while 1==1:

            if new_idea == "":
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
                print(f"Your new main idea {new_main_idea} was added to your list of Mains.")
                break


    def get_idea_type(self):
        """Appending existing ideas with new ideas. """

        retry_limit = 3
        while 1==1:
            choices = ["main","side","set meal", "lunch"]
            idea = input("Main/Side/Set Meal/Lunch?: ")
            if idea.lower() in choices:
                for choice in
                self.add_to_list(idea)
            elif idea == "side":
                print("\nNothing detected. Try again (Retries left: %d)" % retry_limit)
                retry_limit -= 1
                if retry_limit == 0:
                    print("Retry limit reached!")
                    break
            else:
                print("Invalid choice!")


    def display_ideas(self):

        """ Does what it says on the tin - displays the current ideas
            Oh, and makes it look a bit nicer
            # # # TODO: Fix and complete this """

        main_list = self.food_list(0)
        side_list = self.food_list(1)
        set_meal_list = self.food_list(3)
        lunch_list = self.food_list(2)

        print("\nMain ideas: %s (Total: %d)" % str(main_list), len(self.food_list(0)))

FoodGenius().home()