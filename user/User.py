'''
Created on 21 juin 2022

@author: Jules Michaud
'''
class User() :

    def __init__(self, history, constraints):
        '''
        Constructor
        '''
        self.history = history
        self.constraints = constraints
    
    def set_history(self, history):
        self.history = history

    def set_constraints(self, constraints):
        self.constraints = constraints
    
    def get_history(self):
        return self.history

    def get_constraints(self):
        return self.constraints
        
    def constraints_complexity(self, ingredients_type):
        complexity=0
        for constraint in constraints:
            if constraint.get_ingredients_type()==ingredients_type:
                complexity += constraint.constraint_interest()
        return complexity