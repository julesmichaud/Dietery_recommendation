'''
Created on 21 juin 2022

@author: Jules Michaud
'''
class History() :

    def __init__(self, meals, appreciations):
        '''
        Constructor
        '''
        self.meals = meals
        self.appreciations = appreciations
    
    def set_meals(self, meals):
        self.meals = meals

    def set_appreciations(self, appreciations):
        self.appreciations = appreciations
    
    def get_meals(self):
        return self.meals

    def get_appreciations(self):
        return self.appreciations
    
    def add_meal(self, meal):
        self.meals.append(meal)
    
    def add_appreciation(self, appreciation):
        self.appreciations.append(appreciation)
    
    def add_rateed_meal(self, meal, appreciation):
        self.add_meal(meal)
        self.add_appreciation(appreciation)