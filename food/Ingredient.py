'''
Created on 20 juin 2022

@author: Aurelien Giroux
'''


class Ingredient(object):
    '''
    classdocs
    '''

    def __init__(self, ingredient_param):
        '''
        Constructor
        '''
        self.name=ingredient_param[2]  # A string giving the name of the ingredient
        # A string giving the nature of the aliment (carbohydrate, protein etc...)
        #self.set_nature(nature)
        #11000 correspond à une valeur approximative du nombre de participants à inc3'''
        self.average_consumption=(int(ingredient_param[-1])/11000)
        #256301 correspond au nombre d'aliments consommé pendant l'etude inca3'''
        self.popularity_frequency=(int(ingredient_param[-1])/256301)
        # An integer giving the amount of calories per 100 grams of raw aliment
        self.calories_per_hundred_grams=1
        # An integer giving the amount of CO2 emitted by the production of 100g of said aliment
        self.carbon_emissions_per_hundred_grams=1
        # A list of 2 dates giving the approximate period of local availability of the ingredient (used to decide whether it is in season or not)
        self.local_availability_period=1

    def get_name(self):
        return self.name
    
    def get_average_consumption(self):
        return self.average_consumption
    
    def get_popularity_frequency(self):
        return self.popularity_frequency
    

    # def get_nature(self):
    #   return self.nature

    def get_calories_per_hundred_grams(self):
        return self.calories_per_hundred_grams

    def get_carbon_emissions_per_hundred_grams(self):
        return self.carbon_emissions_per_hundred_grams

    def get_local_availability_period(self):
        return self.local_availability_period

    # def set_name(self, name):
    #     self.name = name
    #
    # def set_nature(self, nature):
    #     self.nature = nature
    #
    # def set_calories_per_hundred_grams(self, calories_per_hundred_grams):
    #     self.calories_per_hundred_grams = calories_per_hundred_grams
    #
    # def set_carbon_emissions_per_hundred_grams(self, carbon_emissions_per_hundred_grams):
    #     self.carbon_emissions_per_hundred_grams = carbon_emissions_per_hundred_grams
    #
    # def set_local_availability_period(self, local_availability_period):
    #     self.local_availability_period = local_availability_period
    
    

    def __eq__(self, other):
        return (self.get_name() == other.get_name()) and (self.get_nature() == other.get_nature()) and (self.get_calories_per_hundred_grams() == other.get_calories_per_hundred_grams()) and (self.get_carbon_emissions_per_hundred_grams() == other.get_carbon_emissions_per_hundred_grams()) and (self.get_local_availability_period() == other.get_local_availability_period())
