'''
Created on 21 juin 2022

@author: Jules Michaud
'''

import Constraint

class HardConstraint(Constraint) :

    def __init__(self, ingredients_type):
        '''
        Constructor
        '''
        super.__init__(self,ingredients_type)
   
    def constraint_interest(self):
        return float ('inf')