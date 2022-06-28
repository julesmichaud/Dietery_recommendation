'''
Created on 21 juin 2022

@author: Jules Michaud
'''

class HardConstraints :

    def __init__(self, banned_ingredients):
        '''
        Constructor
        '''
        set_banned_ingredients(banned_ingredients)
        
    def get_banned_ingredients(self):
        return self.banned_ingredients
    
    def set_banned_ingredients(self,banned_ingredients):
        self.banned_ingredients= banned_ingredients
        
    def add_banned_ingredients(self, ingredient):
        self.banned_ingredients.append(ingredient)