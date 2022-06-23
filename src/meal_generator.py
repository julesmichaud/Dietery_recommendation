'''
Created on 22 juin 2022

@author: Aurelien Giroux
'''
from food.alimentary_sequence import Alimentary_sequence
import src.main as main

class MealGenerator(object):
    '''
    classdocs
    '''
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


if __name__ == '__meal_generator__':
    number_of_menus = main.get_number_of_menus()
    ingredients = []
    time = 0
    sequence = Alimentary_sequence.__init__(Alimentary_sequence, ingredients, time) #Alimentary_sequence = self ?