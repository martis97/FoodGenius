import random
import warnings
import re
import exceptions as Err


class FoodGenius(object):
    """
    __"Hmm, what should I cook?"__
    I.e. The Food Genius.
    A console app which randomly chooses an item from given list and outputs it to the user.
    It will provide one of the items from Mains and Sides, and a set meal as an alternative if desired over suggested.
    It will also provide an idea for breakfast the next day.

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
            "breakfast":
                {
                    "file_name" : "breakfast.txt"
                }, 
            "set meal":
                {
                    "file_name": "set_meals.txt"
                }
        }
        self.FG = FoodGenius
        self.retry_limit = 3
    
    def main(self):
        """ Requests the initial option """
        
        print("\n///////Food Genius///////")
        print("Simple console app which suggests meal options.")

        options = \
            {
                "1" :   {
                        "message" : "\n1. Get food suggestions for today",
                        "command" : "self.food_call()"
                        },
                "2" :   {
                        "message" : "2. Add a new suggestion to the list",
                        "command" : "self.get_idea_type()"
                        },
                "3" :   {
                        "message" : "3. Display all available suggestions",
                        "command" : "self.list_all_ideas()"
                        }, 
                "4" :   {
                        "message" : "4. Exit",
                        "command" : None
                        }
            }

        while True:
            print("_____________________________________")

            # Print all available option messages
            for action in options:
                key = options.get(action)
                print(key.get("message"))

            # Get choice number
            choice = input("Answer (number): ")
            while choice == "":
                choice = self.FG.retry(self.retry_limit)
                if choice == "":
                    self.retry_limit -= 1
                else:
                    self.FG.validate_input(int(choice))

            # Check if valid integer
            if not re.match("[0-9]", choice):
                print("\nExpected Int!")
                self.FG.retry(self.retry_limit, new_response=False)
                self.retry_limit -= 1

            # Check if provided is a valid option
            if choice in options:
                option = options[choice]
                if option["command"]:
                    eval(option["command"])
                else:
                    break
            else:
                print("Invalid choice!")
                self.retry_limit -= 1

    def food_list(self, idea_type):
        """Read and return a selected list given its name.

        Args:
            idea_type: The type of list to be returned.
        
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
        user.
        """

        random_main = random.choice(self.food_list("main"))
        random_side = random.choice(self.food_list("side"))
        random_breakfast = random.choice(self.food_list("breakfast"))
        random_set_meal = random.choice(self.food_list("set meal"))

        print(f"\nFor dinner, you can have {random_main} with {random_side}")
        print(f"...or you could have {random_set_meal}")
        print(f"\nFor breakfast tomorrow, you could have {random_breakfast}")
    
    def add_to_list(self, idea_type):
        """Gets the new meal suggestion and adds it to the list given 
        its type.
        
        Args:
            idea_type: Type of idea to be used to get the right list.
        """

        new_idea = input("What's your new meal suggestion?: ")
        self.FG.validate_input(new_idea)

        while True:
            if new_idea == "":
                self.FG.retry(self.retry_limit)
                self.retry_limit -= 1
            elif new_idea in self.food_list(idea_type):
                print("Idea already exists")
                self.FG.retry(self.retry_limit)
                self.retry_limit -= 1
            else:
                meal = self.meals[idea_type]
                path_to_file = "C:/Food Genius/ideas/%s" % meal["file_name"]
                with open(path_to_file, "a") as food_file:
                    food_list = food_file.read().split(",")
                    food_list.append(new_idea)
                    # for item in food_list:
                    # # # TODO: Fix this
                        
    def get_idea_type(self):
        """Appending existing ideas with new ideas."""

        while True:
            choices = [food_type for food_type in self.meals]
            idea_type = input(f"Main/Side/Set Meal/Breakfast?: ")
            self.FG.validate_input(idea_type)
            for choice in choices:
                while idea_type == "":
                    idea_type = self.FG.retry(self.retry_limit)
                    self.retry_limit -= 1
                if idea_type.lower() in choice:
                    self.add_to_list(choice)
                else:
                    print("Invalid choice!")
                    self.retry_limit -= 1
                    self.FG.retry(self.retry_limit, new_response=False)
                    continue

    def list_all_ideas(self):
        """Shows current entries in the lists."""

        mains = ""
        for idea in self.food_list("main"):
            mains += f"{idea}, "

        sides = ""
        for idea in self.food_list("side"):
            sides += f"{idea}, "

        set_meals = ""
        for idea in self.food_list("set meal"):
            set_meals += f"{idea}, "

        breakfasts = ""
        for idea in self.food_list("breakfast"):
            breakfasts += f"{idea}, "

        print("\nMain ideas: %s" % mains.strip("^.+, $"))
        print("Sides ideas: %s" % sides.strip("^.+, $"))
        print("Set Meal ideas: %s" % set_meals.strip("^.+, $"))
        print("Breakfast ideas: %s" % breakfasts.strip("^.+, $"))

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
            illegal_chars = r"^.*[\^\"\'\[\]\$\{\}\(\)\*\+\`,.<>/@&=#%£~!_-].*$"
            if re.match(illegal_chars, input):
                raise Err.InvalidInputException \
                    ("You've entered illegal character(s)")
        if isinstance(input, int):
            if input not in range(0, 5):
                raise Err.InvalidInputException \
                    ("Number out of range")
        
        return True

    @staticmethod
    def retry(retry_limit, new_response=True):
        """Gets a new response if required and checks the retry limit.
        
        Args:
            retry_limit: The retry limit remaining
            new_response: (default: True) Boolean value to specify whether 
                new response is required.
        
        Raises:
            RetryLimitException: Retry limit has been exceeded.
        """

        if new_response:
            new_response = input(f"Try again?(Retries left: {retry_limit}) : ")
            FoodGenius.validate_input(new_response)
        if retry_limit == 0:
            raise Err.RetryLimitException("Retry limit exceeded.")
        
        return new_response



FoodGenius().main()