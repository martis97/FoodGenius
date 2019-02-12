import random
import warnings
import re
import exceptions as Err


class FoodGenius(object):
    """
    __"Hmm, what should I cook?"__
    I.e. The Food Genius
    A console app which randomly chooses an item from given list and outputs it to the user
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
                {   
                    "file_name" : "main.txt"
                },
            "side": 
                {
                    "file_name" : "side.txt"
                },
            "lunch":
                {
                    "file_name" : "lunch.txt"
                }, 
            "set meal":
                {
                    "file_name": "set_meals.txt"
                }
        }
        self.FG = FoodGenius
    
    def home(self):
        """ Requests the initial option """
        
        while 1==1:
            print("\nWhat would you like to do?:")
            print("1. Get food ideas")
            print("2. Add a new idea")
            print("3. Display all existing ideas")
            print("4. Exit")

            choice = input("Answer (number): ")
            self.FG.validate_input(int(choice))

            if choice == "1": 
                self.food_call()
            if choice == "2":
                self.get_idea_type()
            if choice == "3":
                self.list_all_ideas()
            if choice == "4":
                break

    def food_list(self, idea_type):
        """Read and return a selected list given its ID.
        
        Returns:
            food_list: (list) All entries in the file returned in a list.
        """
        
        idea_list = self.meals[idea_type]
        with open("C:/Food Genius/ideas/%s" % idea_list["file_name"], "r")  \
            as food_file:
            
            food_list = food_file.read().split(",")
            return food_list

    def food_call(self):
        """Providing a random item from each list and displaying it to the 
        user 
        """

        random_main = random.choice(self.food_list("main"))
        random_side = random.choice(self.food_list("side"))
        random_lunch = random.choice(self.food_list("lunch"))
        random_set_meal = random.choice(self.food_list("set meal"))

        print(f"For dinner, you can have {random_main} with {random_side}")
        print(f"...or you could have {random_set_meal}")
        print(f"\nFor lunch tomorrow, you could have {random_lunch}")
    
    def add_to_list(self, idea_type):
        """Gets the new idea and adds it to the list given its type.
        
        Args:
            idea_type: Type of idea to be used to get the right list.
        
        Raises:
            RetryLimitException: When retry limit for input exceeds 
                the default amount, which is 3.
        """

        retry_limit = 3
        new_idea = input("What's your new idea?: ")
        self.FG.validate_input(new_idea)
        while True:
            if new_idea == "":
                self.FG.retry(retry_limit)
                retry_limit -= 1
            elif new_idea in self.food_list(idea_type):
                print("Idea already exists")
                self.FG.retry(retry_limit)
                retry_limit -= 1
            else:
                meal = self.meals[idea_type]
                path_to_file = "C:/Food Genius/ideas/%s" % meal["file_name"]
                with open(path_to_file, "a") as food_file:
                    food_list = food_file.read().split(",")
                    food_list.append(new_idea)
                    # for item in food_list:
                        

    def get_idea_type(self):
        """Appending existing ideas with new ideas."""

        retry_limit = 3
        while True:
            retry_reminder = f"(Retries left:{retry_limit})"
            choices = [food_type for food_type in self.meals]
            if retry_limit == 3:
                retry_reminder = ""
            idea = input(f"Main/Side/Set Meal/Lunch?{retry_reminder}: ")
            self.FG.validate_input(idea)
            for choice in choices:
                if idea == "":
                    while idea == "":
                        idea = self.FG.retry(retry_limit)
                        retry_limit -= 1
                elif idea.lower() in choice:
                    self.add_to_list(choice)
                else:
                    continue
            print("Invalid choice!")
            retry_limit -= 1
            self.FG.retry(retry_limit, new_response=False)

    def list_all_ideas(self):
        """ Does what it says on the tin - displays the current ideas
            Oh, and makes it look a bit nicer
            TODO: Fix and complete this 
        """

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

        print("\nMain ideas: %s" % mains.strip("^.+, $"))
        print("Sides ideas: %s" % sides.strip("^.+, $"))
        print("Set Meal ideas: %s" % set_meals.strip("^.+, $"))
        print("Lunch ideas: %s" % lunches.strip("^.+, $"))

    @staticmethod
    def retry(retry_limit, new_response=True):
        if new_response:
            new_response = input(f"Try again?(Retries left: {retry_limit}) : ")
            FoodGenius.validate_input(new_response)
        if retry_limit == 0:
            raise Err.RetryLimitException("Retry limit exceeded.")
        
        return new_response

    @staticmethod
    def validate_input(input):
        """Validates the input from the user side

        Args:
            input: String to be validated
        Raises:
            InavlidInputException: Invalid input detected
        Returns:
            True - Input is valid
        """
        
        if isinstance(input, str):
            illegal_chars = "^.*(\!|\"|\'|\%|£|\~|\$|\#|\{|\}|\(|\)|\*|@|&).*$"
            if re.match(illegal_chars, input):
                raise Err.InvalidInputException \
                    ("You've entered illegal character(s)")
        if isinstance(input, int):
            if input not in range(0,5):
                raise Err.InvalidInputException \
                    ("Number out of range")
        
        return True


FoodGenius().home()