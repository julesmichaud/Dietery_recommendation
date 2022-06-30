'''
Created on 21 juin 2022

@author: Jules Michaud
'''
from math import log2
from user import History
from user import Constraint

class SoftConstraint(Constraint) :

    def __init__(self, ingredients_type_index, importance, max_quantity):
        '''
        Constructor
        '''
        super.__init__(ingredients_type_index, True)
        self.importance = importance #a float between 0 and 1 that specifies the importance of the constraint
        self.max_quantity = max_quantity #the maximal quantity of ingredient in the type you should eat by week
    
        
    def get_importance(self) :
        return self.importance

    def get_max_quantity(self) :
        return self.max_quantity
    
    def set_importance(self, importance):
        self.importance = importance
    
    def set_max_quantity(self, max_quantity):
        self.max_quantity = max_quantity

    
    def constraint_interest(self,n): 
        if (n == self.get_max_quantity()) :
            return float('inf')
        else :
            return -self.get_importance()*log2(abs(n - self.get_max_quantity())/ self.get_max_quantity())

