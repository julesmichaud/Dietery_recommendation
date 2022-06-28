'''
Created on 21 juin 2022

@author: Jules Michaud
'''

import Ingredients

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
    
    def add_rated_meal(self, meal, appreciation):
        self.add_meal(meal)
        self.add_appreciation(appreciation)
        
    def search_ingredient(self, ingredient):
        count = 0
        for i in range (14):
            for elem in (meals[-i]).get_starter:
                if elem == ingredient:
                    count+=1
            for elem in (meals[-i]).get_maincourse:  
                if elem == ingredient:
                    count+=1
            for elem in (meals[-i]).get_dessert:  
                if elem == ingredient:
                    count+=1  
        return count            
    
    def quantity_by_type(self, type_index):            
        count = 0 
        for elem in Ingredients.get_type_from_index(type_index)
            count+= search_ingredient(elem)
        return count