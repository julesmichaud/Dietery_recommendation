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
        ''' Returns the component of the expected simplicity linked to the availability of an ingredient : the less it appears frequently, the more simple it becomes '''
        return log2(365/nbr_of_days)/coefs.Coefficients.ingredient_availability_coef #ici on peut mettre ce coef à 1 et pondérer les autres relativement
    
    def personal_occurence_score(self, nbr_of_personal_occurrences, mean, timespan):
        ''' Returns the component of the observed simplicity linked to the difference between the user's diet and a typical french person's diet '''
        x = nbr_of_personal_occurrences
        return log2(timespan/(1+abs(x-mean)))
        #If a person eats like a typical french person, its description is simple (we just say he eats like a typical french person), : max simplicity of log2(timespan)
        #If a person is really "excentric" and eats like a very abnormal french person, we need to describe him specifically (he is thefore complex, and his simplicity tends to be 0)
    
    def popularity_score(self, popularity_frequency):
        ''' Returns the component of the expected simplicity linked to the popularity of the aliment in the French population '''
        foc = popularity_frequency
        return log2(1/foc)/coefs.Coefficients.popularity_coef
        #The more the ingredient is used in the french diet, the more complex it becomes, so the simplicity score decreases
    
    def kolmogorov_ingredient(self, ingredient, history): #Criteria : in season / physical distance to supermarket / nature of the ingredient
        ''' Returns the agregated simplicity score of the ingredient '''
        nbr_of_days = (ingredient.local_availability_period[1]-ingredient.local_availability_period[0]).days #Number of days of availability of the ingredient during the year
        nbr_of_personal_occurrences = history.search_ingredient(ingredient) #Number of occurrences of the meal during the past week in the history of the user
        popularity_frequency = history.popularity_frequency(ingredient) #Frequence at which the 
        return self.ingredient_availability_score(nbr_of_days) + self.personal_occurence_score(nbr_of_personal_occurrences, 1.5) + self.popularity_score(popularity_frequency)
        
    def kolmogorov_sequence(self, sequence):
        ''' Returns the agregared simplicity score of the whole sequence '''
        interest_score = 0
        for ingredient in sequence.get_ingredients():
            interest_score += self.kolmogorov_aliment(ingredient)
        return interest_score/coefs.Coefficients.normalization_kolmogorov_alimentary_sequence
    
    def explainable_kolmogorov_ingredient(self, ingredient, history):
        ''' Returns the list of the simplicity score components for an ingredient '''
        nbr_of_days = (ingredient.local_availability_period[1]-ingredient.local_availability_period[0]).days #Number of days of availability of the ingredient during the year
        nbr_of_personal_occurrences = history.search_ingredient(ingredient) #Number of occurrences of the meal during the past week in the history of the user
        popularity_frequency = history.popularity_frequency(ingredient) #Frequence at which the 
        return [self.ingredient_availability_score(nbr_of_days), self.personal_occurence_score(nbr_of_personal_occurrences, 1.5), self.popularity_score(popularity_frequency)]
    
    def maj_weights(self, environnement, history, keyword_weights_pairs): #TODO
        return 1