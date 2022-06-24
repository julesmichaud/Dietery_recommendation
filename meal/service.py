'''
Created on Jun 20, 2022

@author: valerio
'''

from food.alimentary_sequence import Alimentary_sequence

class Service(Alimentary_sequence):
    '''
    classdocs
    '''

    def __init__(self, ingredients, time, portion_size):
        '''
        Constructor
        '''
        super.__init__(ingredients, time)
        self.set_portion_size(portion_size) #A float giving the portion size, the standard portion_size use in the recipes is 1.  
        
    def set_portion_size(self, portion_size):
        self.portion_size = portion_size
        
    def adjusted_calories(self): #returns the service's total calories
        return self.portion_size * super.portion_calories(self)
    
    def adjusted_carbon(self): #returns the service's total carbon emission
        return self.portion_size * super.portion_carbon_emission(self)