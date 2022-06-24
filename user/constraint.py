'''
Created on 21 juin 2022

@author: Jules Michaud
'''
class Constraint() :

    def __init__(self, importance, description):
        '''
        Constructor
        '''
        self.importance = importance
        self.description = description
    
    def set_importance(self, importance):
        self.importance = importance
    
    def set_description(self, description):
        self.description = description
    
    def get_importance(self):
        return self.importance
    
    def get_description(self):
        return self.description
     