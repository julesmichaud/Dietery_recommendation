'''
Created on 20 Juin, 2022

@author: Aurelien Giroux
'''

from math import log2, sqrt
import kolmogorov.Coefficients as coefs
from user.User import User
from food.Ingredients import Ingredients

#Doxygen pour générer la doc des fonctions !!

class Kolmogorov(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.ingredient_availability_coef = 1
        self.personal_occurence_coef = 1
        self.popularity_coef = 1
        self.normalization_kolmogorov_alimentary_sequence = 1
        
    def ingredient_availability_score(self, nbr_of_days):
        ''' Returns the component of the simplicity linked to the availability of an ingredient : the less it appears frequently, the more simple it becomes '''
        return log2(365/nbr_of_days)/coefs.Coefficients.ingredient_availability_coef #ici on peut mettre ce coef à 1 et pondérer les autres relativement
    
    def popularity_score(self, popularity_frequency):
        ''' Returns the component of the simplicity linked to the popularity of the aliment in the French population '''
        foc = popularity_frequency
        return log2(1/foc)/coefs.Coefficients.popularity_coef
        #The more the ingredient is used in the French diet, the more complex it becomes, so the simplicity score decreases
    
    def personal_constraint_score(self, ingredient):
        ''' Returns the component of the simplicity linked to the difference between the user's diet and a typical french person's diet '''
        type_index = Ingredients.get_type_index(self, ingredient)
        expectation = Ingredients.get_average_consumption(ingredient)
        excentricity_complexity = User.excentricity_complexity(User, expectation, ingredient)
        if(type_index == 3):
            return User.constraints_complexity(User,3) + excentricity_complexity
        elif(type_index == 4):
            return User.constraints_complexity(User,4) + excentricity_complexity
        return None
    
        #return log2(timespan/(1+abs(x-mean)))
        #If a person eats like a typical French person, its description is simple (we just say he eats like a typical french person), : max simplicity of log2(timespan)
        #If a person is really "excentric" and eats like a very abnormal French person, we need to describe him specifically (he is thefore complex, and his simplicity tends to be 0)
    
    def health_score(self, ingredient):
        ''' Returns the health score '''
    
    def kolmogorov_ingredient(self, ingredient): #Criteria : in season / physical distance to supermarket / nature of the ingredient
        ''' Returns the aggregated simplicity score of the ingredient '''
        availability_period = ingredient.get_local_availability_period(ingredient)
        nbr_of_days = (availability_period[1]-availability_period[0]).days #Number of days of availability of the ingredient during the year
        popularity_frequency = Ingredients.get_popularity_frequency(Ingredients,ingredient)#history.popularity_frequency(ingredient) #Frequence at which the 
        return self.ingredient_availability_score(nbr_of_days) + self.popularity_score(popularity_frequency) - self.personal_constraint_score(ingredient)
        #global_score = surprise_score - constraint_malus
        
    def kolmogorov_sequence(self, sequence):
        ''' Returns the aggregated simplicity score of the whole sequence '''
        interest_score = 0
        for ingredient in sequence.get_ingredients():
            interest_score += self.kolmogorov_aliment(ingredient)
        return interest_score/coefs.Coefficients.normalization_kolmogorov_alimentary_sequence
    
    def explainable_constraint_score(self, ingredient):
        ''' Returns the '''
        type_index = Ingredients.get_type_index(self, ingredient)
        expectation = Ingredients.get_average_consumption(ingredient)
        excentricity_complexity = User.excentricity_complexity(User, expectation, ingredient)
        if(type_index == 3):
            return [User.constraints_complexity(User,3), excentricity_complexity]
        elif(type_index == 4):
            return [User.constraints_complexity(User,4), excentricity_complexity]
        return None
    
    def explainable_kolmogorov_ingredient(self, ingredient)
        ''' Returns the list of the simplicity score components for an ingredient '''
        availability_period = ingredient.get_local_availability_period(ingredient)
        nbr_of_days = (availability_period[1]-availability_period[0]).days #Number of days of availability of the ingredient during the year
        popularity_frequency = Ingredients.get_popularity_frequency(Ingredients,ingredient)#history.popularity_frequency(ingredient) #Frequence at which the 
        return [self.ingredient_availability_score(nbr_of_days), self.popularity_score(popularity_frequency)] + self.personal_constraint_score(ingredient)
    
    def maj_weights(self, environnement, history, keyword_weights_pairs): #TODO
        return 1