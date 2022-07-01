'''
Created on 21 juin 2022

@author: Jules Michaud
'''

from meal.meal import Meal
from math import log2, fabs
from food.Ingredients import Ingredients
from food.Ingredient import Ingredient
class History() :
    '''
    This class traces the history of the meals eaten by the user, as a list of meals. For the moment, the history is not saved between one use of the app and another
    '''

    def __init__(self, meals):
        '''
        Constructor
        '''
        self.meals = meals
    
    def set_meals(self, meals):
        self.meals = meals
    
    def get_meals(self):
        return self.meals
    
    def add_meal(self, meal):
        self.meals.append(meal)
    
        
    def search_ingredient(self, ingredient):
        count = 0
        for i in range(1,15): #commencer � 1 pour prendre le repas d'indice -1, i.e. le dernier, finir � -15 pour le 14�me avant la fin
            for j in range(len(self.get_meals()[-i])):
                alimentary_sequence = self.get_meals()[-i][j]
                for elem in alimentary_sequence.get_ingredients():
                    if elem.get_name() == ingredient.get_name():
                        count+=1 
        return count            
    
    def quantity_by_type(self, type_index):            
        count = 0 
        for elem in Ingredients.get_type_from_index(type_index):
            count+= self.search_ingredient(elem)
        return count
    
    def get_last_meal(self):
        return self.get_meals()[-1]
    
    
    