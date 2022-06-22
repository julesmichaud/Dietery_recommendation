'''
Created on Jun 20, 2022

@author: valerio
'''

from datetime import *

class Alimentary_sequence:
    '''
    classdocs
    '''

    def __init__(self, ingredients, time):
        '''
        Constructor
        '''
        self.set_ingredients(ingredients)#A list of [ingredient, quantity], where quantity is the quantity of ingredient necessary to make the recipe
        self.set_time(time)#The time necessary to make the recipe
        
    def set_ingredients(self, ingredients):
        self.ingredients = ingredients
        
    def set_time(self, time):
        self.time = time
    
    def get_ingredients(self):
        return self.ingredients
    
    def get_time(self):
        return self.time
    
    def portion_calories(self): #returns the calories for one portion
        cal=0
        for [ingredient, quantity] in self.ingredients:
            cal+= (quantity/100)*ingredient.calories_per_hundred_grams
        return cal

    def portion_carbon_emission(self): #returns the carbon emission for one portion   
        carb=0
        for [ingredient, quantity] in self.ingredients:
            carb+= (quantity/100)*ingredient.carbon_emissions_per_hundred_grams
        return carb
    
    def local_avaibility_period(self): #returns the local availability period of the recipe
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
        
    
    
            
            