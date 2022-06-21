'''
Created on Jun 20, 2022

@author: Aur�lien
'''
#from src import Ingredient
from math import log2
from math import ceil
import kolmogorov.Coefficients.Coefficients as coefs

class Kolmogorov(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    def kolmogorov_ingredient(self, ingredient):
        nbr_of_days = (ingredient.local_availability_period[1]-ingredient.local_availability_period[0]).days
        return ceil((log2(nbr_of_days/365) - log2(1/365))/coefs.normalization_kolmogorov_ingredient)
        #Si un ingr�dient n'existe qu'un jour par an, il est tr�s inattendu, sa complexit� souhait�e est donc log2(1/365) - log2(1/365) = 0
        #Si un ingr�dient existe au contraire toute l'ann�e, on veut qu'il ait une grande complexit� soit log2(365/365) - log2(1/365) = log2(365) = 8,5 environ
    
    def kolmogorov_recipe(self, recipe):
        complexity = 0
        for ingredient in recipe.get_ingredients():
            complexity += self.kolmogorov_aliment(ingredient)
        return complexity/coefs.normalization_kolmogorov_recipe
    
    def maj_weights(self, environnement, history, keyword_weights_pairs): #TODO
        return 1