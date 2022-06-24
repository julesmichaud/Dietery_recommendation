'''
Created on 22 juin 2022

@author: Aurelien Giroux
'''
from food.alimentary_sequence import Alimentary_sequence

def generate_meal(number_of_menus):
    ingredients = [] #To initialize with the ingredients of the last meal
    time = 0
    print("Generating " + str(number_of_menus) + " menus...")
    sequence = Alimentary_sequence(ingredients, time)
    print("Done ! Here you go ;)")
    print(sequence)

if __name__ == '__main__':
    generate_meal()