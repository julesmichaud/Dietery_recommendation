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
        self.constraints = constraints #a list of constraint
    
    def set_history(self, history):
        self.history = history

    def set_constraints(self, constraints):
        self.constraints = constraints
    
    def get_history(self):
        return self.history

    def get_constraints(self):
        return self.constraints
        
    def constraints_complexity(self, ingredients_type_index): #returns the complexity due to the constraints for a specified type
        complexity=0
        for constraint in self.constraints:
            if constraint.get_ingredients_type_index()==ingredients_type_index:
                if constraint.get_is_soft():
                    n=history.quantity_by_type(ingredients_type_index)
                    complexity+=constraint.constraint_interest(n)
                else:
                    complexity += constraint.constraint_interest()
        return complexity
    
    def excentricity_complexity(self, expectation, ingredient): #returns the complexity due to the excentricity of the actual alimentation of the user
        return  log2(28/(1+abs(history.search_ingredient(ingredient)-expectation)))