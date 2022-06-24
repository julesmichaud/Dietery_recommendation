'''
Created on 22 juin 2022

@author: Aurelien Giroux
'''
from food.alimentary_sequence import Alimentary_sequence
import src.main as main
from asyncio.tasks import sleep

class MealGenerator(object):
    '''
    classdocs
    '''

if __name__ == '__Meal_generator__':
    number_of_menus = main.get_number_of_menus()
    ingredients = [] #To initialize with the ingredients of the last meal
    time = 0
    print("Generating " + number_of_menus + " menus...")
    sleep(1)
    sequence = Alimentary_sequence()
    print("Done ! Here you go ;)")
    print(sequence)