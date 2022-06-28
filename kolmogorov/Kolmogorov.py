'''
Created on 20 Juin, 2022

@author: Aurelien Giroux
'''

from math import log2, sqrt
import kolmogorov.Coefficients as coefs

##Important
#Doxygen pour générer la doc des fonctions !!
#import qrcode pour générer le qrcode vers le git sur le poster !!

class Kolmogorov(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        
    def ingredient_availability_score(self, nbr_of_days):
        return log2(365/nbr_of_days)/coefs.Coefficients.ingredient_availability_coef #ici on peut mettre ce coef à 1 et pondérer les autres relativement
    
    def personal_occurence_score(self, nbr_of_personal_occurrences, mean, timespan):
        x = nbr_of_personal_occurrences
        return log2(timespan/(1+abs(x-mean)))
        #q = filter_quality_factor
        #return log2(0.5 + 1/sqrt((1-(x-0.1)**2)**2+((x-0.1)/q)**2))/coefs.personal_occurence_coef
    
    def popularity_score(self, popularity_frequency):
        foc = popularity_frequency
        return log2(1/foc)/coefs.Coefficients.popularity_coef
    
    def kolmogorov_ingredient(self, ingredient, history): #Criteria : in season / physical distance to supermarket / nature of the ingredient
        nbr_of_days = (ingredient.local_availability_period[1]-ingredient.local_availability_period[0]).days #Number of days of availability of the ingredient during the year
        nbr_of_personal_occurrences = history.search_ingredient(ingredient) #Number of occurrences of the meal during the past week in the history of the user
        popularity_frequency = history.popularity_frequency(ingredient) #Frequence at which the 
        return self.ingredient_availability_score(nbr_of_days) + self.personal_occurence_score(nbr_of_personal_occurrences, 1.5) + self.popularity_score(popularity_frequency)
        
    def kolmogorov_sequence(self, sequence):
        interest_score = 0
        for ingredient in sequence.get_ingredients():
            interest_score += self.kolmogorov_aliment(ingredient)
        return interest_score/coefs.Coefficients.normalization_kolmogorov_alimentary_sequence
    
    def maj_weights(self, environnement, history, keyword_weights_pairs): #TODO
        return 1