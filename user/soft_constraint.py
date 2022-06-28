'''
Created on 21 juin 2022

@author: Jules Michaud
'''
from math import log2
import History

class SoftConstraint() :

    def __init__(self, ingredients_type, importance, max_quantity, history):
        '''
        Constructor
        '''
        self.importance = importance
        self.max_quantity = max_quantity
        self.history = history
        self.ingredients_type = ingredients_type
    
    def get_importance(self) :
        return self.importance

    def get_max_quantity(self) :
        return self.max_quantity
    
    def get_history(self) :
        return self.history.get_history()
    
    def get_ingredients_type(self) :
        return self.ingredients_type

    def set_importance(self, importance):
        self.importance = importance
    
    def set_max_quantity(self, max_quantity):
        self.max_quantity = max_quantity
    
    def set_history(self, history):
        self.history = history
    
    def set_ingredients_type(self, ingredients_type):
        self.ingredients_type = ingredients_type
    
    def constraint_interest(self):
        meals = self.get_history().get_meals()
        n = 0
        for ingredient in self.get_ingredients_type() :
            n += meals.count(ingredient)
        if (n == self.get_max_quantity()) :
            return float('inf')
        else :
            return -log2(abs(n - self.get_max_quantity())/ self.get_max_quantity())

