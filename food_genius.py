import random
import warnings
import re
import exceptions as Err
import json


class FoodGenius(object):
    """
    __"Hmm, what should I cook?"__
    I.e. The Food Genius.
    A console app which randomly chooses an item from given list and outputs it to the user.
    It will provide one of the items from Mains and Sides, and a set meal as an alternative if desired over suggested.
    It will also provide an idea for breakfast the next day.

    TODO: 
        -> Transform this console app to a web app:
            - Build a Django web app
            - Modify current functions to work as a backend
            - Build nice-to-use front-end and join it with this script.
    """
    
    def __init__(self):
        self.retry_limit = 3
        self.json_path = "C:/Food Genius/ideas.json" 
        with open(self.json_path, "r") as meals:
            self.meals = json.loads(meals.read())
        self.mains = self.meals["main"]
        self.sides = self.meals["side"]
        self.set_meals = self.meals["set meal"]
        self.breakfasts = self.meals["breakfast"]
        self.FG = FoodGenius
    
    def main(self):
        """ Requests the initial option """
        
        print("\n///////Food Genius///////")
        print("Simple console app which suggests meal options.")

        options = \
            {
                1 :   {
                        "message" : "\n1. Get food suggestions for today",
                        "command" : "self.food_call()"
                        },
                2 :   {
                        "message" : "2. Add a new suggestion to the list",
                        "command" : "self.add_suggestion()"
                        },
                3 :   {
                        "message" : "3. Remove a suggestion from list",
                        "command" : "self.remove_suggestion()"
                        },
                4 :   {
                        "message" : "4. Display all available suggestions",
                        "command" : "self.list_all_suggestions()"
                        }, 
                5 :   {
                        "message" : "5. Exit",
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
            try:
                choice = int(input("Answer (number): "))
            except ValueError:
                print("ERROR: Expected Integer!")
                
            while not choice:
                choice = self.FG.retry(self.retry_limit)
                self.retry_limit -= 1

            # Check if provided is a valid option
            if choice in options:
                option = options[choice]
                if option["command"]:
                    eval(option["command"])
                else:
                    break
            else:
                print("\nERROR: Invalid choice!")
                self.retry_limit -= 1
                self.FG.retry(self.retry_limit, new_response=False)
                continue

    def food_call(self):
        """Providing a random item from each list and displaying it to the
        user.
        """

        for meal_type in self.meals:
            meal_type = meal_type.replace(" ", "_")
            globals()[f"random_{meal_type}"] = \
                eval("random.choice(self.%ss)" % meal_type)

        print(f"\nFor dinner, you can have {random_main} with {random_side}")
        print(f"...or you could have {random_set_meal}")
        print(f"\nFor breakfast tomorrow, you could have {random_breakfast}")
    
    def add_to_list(self, idea_type):
        """Gets the new meal suggestion and adds it to the list given 
        its type.
        
        Args:
            idea_type: Type of idea to be used to get the right list.
        """
        
        idea_type = idea_type.replace(" ","_")
        while True:
            new_idea = input("What's your new meal suggestion?: ")
            self.FG.validate_input(new_idea)
            if new_idea == "":
                new_idea = self.FG.retry(self.retry_limit)
                self.retry_limit -= 1
            elif new_idea in self.meals[idea_type]:
                print("Suggestion already exists")
                new_idea = self.FG.retry(self.retry_limit)
                self.retry_limit -= 1
            else:
                eval("self.%ss.append(new_idea.title())" % idea_type)
                self.meals[idea_type] = eval("self.%ss" % idea_type)
                with open(self.json_path, "w") as meals_json:    
                    json.dump(self.meals, meals_json, indent=4)

                print(f"'{new_idea.title()}' "
                    f"has been added to the '{idea_type}s' list.")

                break
            
                        
    def get_suggestion_type(self):
        """Appending existing ideas with new ideas.
        
        Returns:
            meal_type: (Str) The type of meal 
        """

        while True:
            idea_type = input(f"Main/Side/Set Meal/Breakfast?: ")
            self.FG.validate_input(idea_type)

            while idea_type == "":
                idea_type = self.FG.retry(self.retry_limit)
                self.retry_limit -= 1

            if idea_type.lower() in [meal_type for meal_type in self.meals]:
                return idea_type
                
            else:
                print("Invalid choice!")
                self.retry_limit -= 1
                self.FG.retry(self.retry_limit, new_response=False)

    def add_suggestion(self):
        """Adds a suggestion from the list."""

        suggestion_type = self.get_suggestion_type()
        self.add_to_list(suggestion_type)
    
    def remove_suggestion(self):
        """Removes a suggestion from the list."""

        suggestion_type = self.get_suggestion_type().replace(" ", "_")
        suggestion_list = eval(f"self.{suggestion_type}s")

        print("Select which suggestion you would like to remove:")
        number = 1
        for entry in suggestion_list:
            print(f"{number}. {entry}")
            number += 1

        choice = input("Number: ")

		# Check if valid integer
        while not choice.isnumeric():
            print("\nERROR: Expected Int!")
            self.retry_limit -= 1
            choice = self.FG.retry(self.retry_limit)
				
        self.FG.validate_input(int(choice))

        while not choice:
            choice = self.FG.retry(self.retry_limit)
            self.FG.validate_input(choice)
            self.retry_limit -= 1
        
        suggestion_list = eval(f"self.{suggestion_type}s")

        print(f"Removing '{suggestion_list[int(choice)-1]}' " 
            f"from the list of {suggestion_type}s.")

        eval(f"self.{suggestion_type}s.pop({int(choice)-1})")

        self.meals[suggestion_type] = eval(f"self.{suggestion_type}s")
        with open(self.json_path, "w") as meals_json:
            json.dump(self.meals, meals_json, indent=4)

    def list_all_suggestions(self):
        """Shows current entries in the lists."""

        for meal_type in self.meals:
            meal_type = meal_type.replace(" ", "_")
            globals()[f'{meal_type}s'] = ""
            for idea in eval(f"self.{meal_type}s"):
                globals()[f"{meal_type}s"] += f"{idea}, "
            
            title = meal_type.capitalize().replace("_", " ")
            all_entries = f"{title} ideas: {globals()['%ss' % meal_type]}"
            print(all_entries.strip("^.+, $"))

    @staticmethod
    def validate_input(user_input):
        """Validates the input from the user side

        Args:
            user_input: String to be validated

        Raises:
            InavlidInputException: Invalid input detected

        Returns:
            True - Input is valid
        """
        
        if isinstance(user_input, str):
            illegal_chars = r"^.*[\^\"\'\[\]\$\{\}\(\)\*\+\`,.<>/@&=#%£~!_-].*$"
            if re.match(illegal_chars, user_input):
                raise Err.InvalidInputException \
                    ("You've entered illegal character(s)")
        if isinstance(user_input, int):
            if user_input < 0:
                raise Err.InvalidInputException \
                    ("Choice must be positive number")
            if user_input not in range(0, 10):
                raise Err.InvalidInputException("Number out of range")
        
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

        if retry_limit == 0:
            raise Err.RetryLimitException("Retry limit exceeded.")

        if new_response:
            new_response = input(f"Try again?(Retries left: {retry_limit}) : ")
            FoodGenius.validate_input(new_response)
            return new_response

if __name__ == "__main__":
    FoodGenius().main()