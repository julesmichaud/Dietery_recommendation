'''
Created on 20 juin 2022

@author: Aurélien Giroux
'''

class Ingredient(object):
    '''
    classdocs
    '''

    def __init__(self, name, nature, calories_per_hundred_grams, carbon_emissions_per_hundred_grams, local_availability_period):
        '''
        Constructor
        '''
        self.set_name(name) #A string giving the name of the ingredient
        self.set_nature(nature) #A string giving the nature of the aliment (carbohydrate, protein etc...)
        self.set_calories_per_hundred_grams(calories_per_hundred_grams) #An integer giving the amount of calories per 100 grams of raw aliment
        self.set_carbon_emissions_per_hundred_grams(carbon_emissions_per_hundred_grams) #An integer giving the amount of CO2 emitted by the production of 100g of said aliment
        self.set_local_availability_period(local_availability_period) #A list of 2 dates giving the approximate period of local availability of the ingredient (used to decide whether it is in season or not)
    
    def set_name(self, name):
        self.name = name
    
    def set_nature(self, nature):
        self.nature = nature
    
    def set_calories_per_hundred_grams(self, calories_per_hundred_grams):
        self.calories_per_hundred_grams = calories_per_hundred_grams
    
    def set_carbon_emissions_per_hundred_grams(self, carbon_emissions_per_hundred_grams):
        self.carbon_emissions_per_hundred_grams = carbon_emissions_per_hundred_grams
    
    def set_local_availability_period(self, local_availability_period):
        self.local_availability_period = local_availability_period