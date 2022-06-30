'''
Created on 21 juin 2022

@author: Jules Michaud
'''

import Constraint

class HardConstraint(Constraint) :

    def __init__(self, ingredients_type_index):
        '''
        Constructor
        '''
        super.__init__(self,ingredients_type_index, False)
   
    def constraint_interest(self):
        return float ('inf')