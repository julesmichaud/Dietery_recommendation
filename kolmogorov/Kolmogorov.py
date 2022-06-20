'''
Created on Jun 20, 2022

@author: Aurélien
'''
from src import Ingredient
from math import log2

class Kolmogorov(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    def kolmogorov_aliment(self, ingredient):
        return log2((ingredient.local_availability_period[1]-ingredient.local_availability_period[0])/365) - log2(1/365)
        #Si un ingrédient n'existe qu'un jour par an, il est très inattendu, sa complexité souhaitée est donc log2(1/365) - log2(1/365) = 0
        #Si un ingrédient existe au contraire toute l'année, on veut qu'il ait une grande complexité soit log2(365/365) - log2(1/365) = log2(365) = 8,5 environ
    
    def kolmogorov_recette(self, recipe):
        complexity = 0
        for ingredient in recipe.get_ingredients():
            complexity += self.kolmogorov_aliment(ingredient)
        return complexity
    
    def maj_weights(self, environnement, history, keyword_weights_pairs): #TODO
        return 1