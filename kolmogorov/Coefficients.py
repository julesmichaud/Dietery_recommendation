'''
Created on 21 juin 2022

@author: Aurélien Giroux
'''

class Coefficients(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.normalization_kolmogorov_ingredient = 1
        self.normalization_kolmogorov_alimentary_sequence = 1
        self.keyword_influence_coefficients_pairs = {}
        #etc... incomplete list, which values have to be updated according to our needs
        
    def add_keyword_influence_coefficients_pairs(self, keyword, coefficient):
        self.keyword_influence_coefficients_pairs[keyword] = coefficient
    
    def update_keyword_influence_coefficients_pairs(self, keyword, new_coefficient):
        if keyword in self.keyword_influence_coefficients_pairs: #Only looks at the keys in the dictionary
            self.keyword_influence_coefficients_pairs.update({keyword : new_coefficient})
            
    def delete_keyword_influence_coefficients_pairs(self, keyword):
        self.keyword_influence_coefficients_pairs.pop(keyword)