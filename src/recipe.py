'''
Created on Jun 20, 2022

@author: valerio
'''

from datetime import *

class Recipe:
    '''
    classdocs
    '''


    def __init__(self, ingredients, time):
        '''
        Constructor
        '''
        self.set_ingredients(ingredients)
        self.set_time(time)
        
    def set_ingredients(self, ingredients):
        self.ingredients = ingredients
        
    def set_time(self, time):
        self.time = time
    
    def get_ingredients(self):
        return self.ingredients
    
    def get_time(self):
        return self.time
    
    def portion_calories(self):
        cal=0
        for [ingredient, quantity] in self.ingredients:
            cal+= (quantity/100)*ingredient.calories_per_hundred_grams
        return cal

    def portion_carbon_emission(self):    
        carb=0
        for [ingredient, quantity] in self.ingredients:
            carb+= (quantity/100)*ingredient.carbon_emissions_per_hundred_grams
        return carb
    
    def local_avaibility_period(self):
        mindate=(self.ingredients[0][0].get_local_availability_period)[0]
        maxdate=(self.ingredients[0][0].get_local_availability_period)[1]
        for elem in self.ingredients:
            startdate= (elem[0].get_local_availability_period)[0]
            enddate= (elem[0].get_local_availability_period)[1]
            if startdate>mindate:
                mindate=startdate
            if enddate<maxdate:
                maxdate=enddate
        return [mindate,maxdate]
        
    
    
            
            