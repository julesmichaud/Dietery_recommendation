'''
Created on 21 juin 2022

@author: Jules Michaud
'''
from abc import ABC

class Constraint(ABC) :

    def __init__(self, ingredients_type):
        '''
        Constructor
        '''
        self.importance = ingredients_type
    
    def set_ingredients_type(self, ingredients_type):
        self.ingredients_type = ingredients_type
    
   
    def get_ingredients_type(self):
        return ingredients_type
    
    @abstractmethod
    def constraint_interest(self):
        pass 
    