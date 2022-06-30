'''
Created on 21 juin 2022

@author: Jules Michaud
'''

from meal.meal import Meal
from math import log2, fabs
from food.Ingredients import Ingredients
from food.Ingredient import Ingredient
class History() :

    def __init__(self, meals, appreciations):
        '''
        Constructor
        '''
        self.meals = meals
        self.appreciations = appreciations
    
    def set_meals(self, meals):
        self.meals = meals

    def set_appreciations(self, appreciations):
        self.appreciations = appreciations
    
    def get_meals(self):
        return self.meals

    def get_appreciations(self):
        return self.appreciations
    
    def add_meal(self, meal):
        self.meals.append(meal)
    
    def add_appreciation(self, appreciation):
        self.appreciations.append(appreciation)
    
    def add_rated_meal(self, meal, appreciation):
        self.add_meal(meal)
        self.add_appreciation(appreciation)
        
    def search_ingredient(self, ingredient):
        count = 0

        for i in range(1,15): #commencer � 1 pour prendre le repas d'indice -1, i.e. le dernier, finir � -15 pour le 14�me avant la fin
            for alimentary_sequence in (self.get_meals()[-i]):
                for elem in alimentary_sequence.get_ingredients:
                    if Ingredient.get_name(elem) == Ingredient.get_name(ingredient): 
                        count+=1  
        return count            
    
    def quantity_by_type(self, type_index):            
        count = 0 
        for elem in Ingredients.get_type_from_index(type_index):
            count+= self.search_ingredient(elem)
        return count
    
    def get_last_meal(self):
        return self.get_meals()[-1]
    
    
    