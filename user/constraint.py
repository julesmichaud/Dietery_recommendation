'''
Created on 21 juin 2022

@author: Jules Michaud
'''
from abc import ABC

class Constraint(ABC) :

    def __init__(self, ingredients_type_index):
        '''
        Constructor
        '''
        self.importance = ingredients_type_index
    
    def set_ingredients_type_index(self, ingredients_type_index):
        self.ingredients_type_index = ingredients_type_index
    
   
    def get_ingredients_type_index(self):
        return ingredients_type_index
    
    @abstractmethod
    def constraint_interest(self):
        pass 
    