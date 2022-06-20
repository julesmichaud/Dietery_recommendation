'''
Created on Jun 20, 2022

@author: valerio
'''

from src.recipe import Recipe

class Service(Recipe):
    '''
    classdocs
    '''


    def __init__(self, ingredients, time, quantity):
        '''
        Constructor
        '''
        super.__init__(ingredients, time)
        self.set_quantity(quantity) 
        
    def set_quantity(self, quantity):
        self.quantity = quantity
        
    def adjusted_calories(self):
        return self.quantity * super.portion_calories(self)
        