import random
import warnings


class FoodGenius(object):
    """
    __"Hmm, what should I cook?"__
    I.e. The Food Genius
    A script which randomly chooses an item from a list and outputs it to the user
    It will provide one of the items from Mains and Sides, and a set meal as an alternative if desired over suggested 
    It will also provide an idea for lunch

    TODO: 
        -> Split some functions to different classes:
            # Put all ideas to JSON file
            # Keep the rest to this class as it is and improve it.

    """
    
    def __init__(self):
        self.meals = {
            "main": 
                {   "file_name" : "main.txt",
                    "id" : 1
                },
            "side": 
                {
                    "file_name" : "side.txt",
                    "id" : 2
                },
            "lunch":
                {
                    "file_name" : "lunch.txt",
                    "id" : 3
                }, 
            "set meal":
                {
                    "file_name": "set_meals.txt",
                    "id" : 4
                }
        }
    
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
                self.get_idea_type()

            elif choice == "3":
                self.display_ideas()

            elif choice == "4":
                break

            else:
                print("\nInvalid choice!")

    def food_list(self, idea_type):
        """Read and return a selected list given its ID.
        
        Returns:
            food_list: (list) All entries in the file returned in a list.
        """

        with open("C:/Food Genius/ideas/%s" % self.meals[idea_type["file_name"]], "r")  \
            as food_file:
            
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

        retry_limit = 3
        while 1==1:
            new_idea = input("What's your new idea?: ")
            if new_idea == "":
                print("Nothing has been entered")
                new_idea = input(f"Try again?(Retries left: {retry_limit}) : ")
                retry_limit -= 1
                if retry_limit == 0:
                    break
            elif new_idea in self.food_list(idea_type):
                print("Idea already exists")
                new_idea = input(f"Try again?(Retries left: {retry_limit}) : ")
                retry_limit -= 1
                if retry_limit == 0:
                    print("Retry limit exceeded.")
                    break
            else:
                with open("C:/Food Genius/ideas/%s" % self.meals[idea_type["file_name"]], "a")  \
                    as food_file:

                    food_list = food_file.read().split(",")
                    food_list.write(new_idea)

    def get_idea_type(self):
        """Appending existing ideas with new ideas. """

        retry_limit = 3
        while 1==1:
            retry_reminder = f"(Retries left:{retry_limit})"
            choices = ["main", "side", "set meal", "lunch"]
            if retry_limit == 3:
                retry_reminder = ""
            idea = input(f"Main/Side/Set Meal/Lunch?{retry_reminder}: ")
            for choice in choices:
                if idea.lower() in choice:
                    self.add_to_list(choice)
                elif idea is None:
                    print(f"Nothing detected. Try again (Retries left: {retry_limit})")
                    retry_limit -= 1
                    if retry_limit == 0:
                        print("Retry limit exceeded!")
                        break
                else:
                    print("Invalid choice!")


    def display_ideas(self):

        """ Does what it says on the tin - displays the current ideas
            Oh, and makes it look a bit nicer
            # # # TODO: Fix and complete this """

        mains = ""
        for idea in self.food_list("main"):
            mains += f"{idea}, "

        sides = ""
        for idea in self.food_list("side"):
            sides += f"{idea}, "

        set_meals = ""
        for idea in self.food_list("set meal"):
            set_meals += f"{idea}, "

        lunches = ""
        for idea in self.food_list("lunch"):
            lunches += f"{idea}, "

        print(f"\nMain ideas: {mains}")
        print(f"Sides ideas: {sides}")
        print(f"Set Meal ideas: {set_meals}")
        print(f"Lunch ideas: {lunches}")

FoodGenius().home()
