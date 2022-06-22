'''
Created on 22 juin 2022

@author: Aurelien Giroux
'''
#The main needs to do the following :
# - Take as an input whether the user wants to configure the program or if it wants to generate menus
#    - If it wants configurations, ask the user what parameters he wants to change, and direct him to the appropriate menu of the program
#    - If it wants to generate menus, ask how many the user wants
# - After being done with a menu, always redirect to the previous menu. Always offer a "go back" option
from click._compat import raw_input
from asyncio.tasks import sleep
from comtypes._comobject import catch_errors

def is_back(user_in):
    str.lower(user_in)
    if(user_in.__eq__("back")):
        return True
    return False

def is_exit(user_in):
    str.lower(user_in)
    if(user_in.__eq__("exit")):
        return True
    return False

def meal_arg_input():
    number_str = raw_input("Please indicate how many menus you would like to generate\n")
    try:
        number_int = int(number_str)
    except:
        print("Please type a number")
        number_int = meal_arg_input()
    return number_int

def wrong_input():
    user_in = raw_input("Type '1' to change your parameters and '2' to generate a meal. At any moment, type 'back' to go back and 'exit' to exit\n")
    if(is_back(user_in) or is_exit(user_in)):
        print("See you soon !")
        exit(0)
    elif(user_in.__eq__("1")):
        print("Temporary menu placeholder")
        #Find a way to execute the general_menu file...
    elif(user_in.__eq__("2")):
        number_of_menus = meal_arg_input()
        print("Temporary meal generator placeholder, with" + str(number_of_menus) + "menus")
        #Find a way to execute the execute meal_generator, or create a generator and generate a menu here
    else:
        print("Unrecognized input, please try again")
        wrong_input()

if __name__ == '__main__':
    number_of_menus = 0
    print("Welcome ! Would you like to modify your personal parameters or to generate a meal ?");
    
    user_in = raw_input("Type '1' to change your parameters and '2' to generate a meal. At any moment, type 'back' to go back and 'exit' to exit\n")
    if(is_back(user_in) or is_exit(user_in)):
        print("See you soon !")
        exit(0)
    elif(user_in.__eq__("1")):
        print("Temporary menu placeholder")
        #Find a way to execute the general_menu file...
    elif(user_in.__eq__("2")):
        number_of_menus = meal_arg_input()
        print("Temporary meal generator placeholder, with " + str(number_of_menus) + " menu(s)")
        #Find a way to execute the execute meal_generator, or create a generator and generate a menu here
    else:
        print("Unrecognized input, please try again")
        wrong_input();