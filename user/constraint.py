'''
Created on 21 juin 2022

@author: Jules Michaud
'''
from abc import ABC

class Constraint(ABC) :

    def __init__(self, ingredients_type_index, is_soft):
        '''
        Constructor
        '''
        self.ingredients_type_index = ingredients_type_index
        self.is_soft = is_soft
    
    def set_ingredients_type_index(self, ingredients_type_index):
        self.ingredients_type_index = ingredients_type_index
    
    def set_is_soft(self, is_soft):
        self.is_soft = is_soft

    def get_ingredients_type_index(self):
        return self.ingredients_type_index
    
    def get_ingredients_is_soft(self):
        return self.is_soft
    
    def constraint_interest(self): #returns the constraint interest
        pass
    