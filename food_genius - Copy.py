# file = open("C:/Users/User/Desktop/The vicious Snake/Food Genius/main.txt","w")
# lunch = file.read().strip("'").split(",")
# new_idea = input("Enter your new idea: ")

# file.write(", " + new idea)

# main_file = "C:/Users/User/Desktop/The vicious Snake/Food Genius/main.txt"

# with open(main_file, "r") as f:
#     mains = f.read().split(",")
#     print(mains)


# with open(main_file,"a+") as f: 
#     new_idea = input("Add your new main idea: ")
#     if new_idea in mains:
#         print("Idea already exists")
#     else:
#         f.write("," + new_idea)

# print(mains)


def food_list(list_id):

    lists = ["main.txt", # list_id = 0
             "side.txt", # list_id = 1
             "lunch.txt", # list_id = 2
             "set_meals.txt"] # list_id = 3

    with open("C:/Users/User/Desktop/The vicious Snake/Food Genius/" + lists[list_id], "r") as food_file:
        food_list = food_file.read().split(",")
        return food_list


list_mains = food_list(4)

print(list_mains[1])



#with open("C:/Users/User/Desktop/The vicious Snake/Food Genius/main.txt","a") as f:
