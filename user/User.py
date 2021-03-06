'''
Created on 21 juin 2022

@author: Jules Michaud
'''
from math import log2
from user.History import History
from user.constraint import Constraint
import random

class User() :
    '''
    Stores the history and constraints linked to a specific. For the moment, the user's profile is not saved between one use of the app and another.
    '''

    def __init__(self, history, constraints):
        '''
        Constructor
        '''
        ingredient_type_index = constraints [0]
        is_soft = constraints[1]
        self.history = History(history)
        self.constraints = [Constraint(ingredient_type_index,is_soft)] #a list of constraints
    
    def set_history(self, history):
        self.history = history

    def set_constraints(self, constraints):
        self.constraints = constraints
    
    def get_history(self):
        return self.history

    def get_constraints(self):
        return self.constraints
        
    def constraints_complexity(self, ingredients, ingredients_type_index): #returns the complexity due to the constraints for a specified type
        complexity=0
        for constraint in self.constraints:
            if constraint.get_ingredients_type_index()==ingredients_type_index:
                if constraint.get_ingredients_is_soft():
                    n=self.history.quantity_by_type(ingredients, ingredients_type_index)
                    complexity+=constraint.constraint_interest()
                else:
                    complexity += constraint.constraint_interest()
        complexity = random.randint(0,300)
        return complexity
    
    def excentricity_complexity(self, expectation, ingredient): #returns the complexity due to the excentricity of the actual alimentation of the user
        return  log2(28/(1+abs(self.history.search_ingredient(ingredient)-expectation)))
    
    def get_last_user_meal(self):
        return self.history.get_last_meal()
    
    def store_user_meal(self,meal):
        self.history.add_meal(meal)
    