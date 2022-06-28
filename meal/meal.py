'''
Created on Jun 20, 2022

@author: Valerio Guerrini
'''

class Meal:
    '''
    classdocs
    '''


    def __init__(self, starter, maincourse, dessert):
        '''
        Constructor
        '''
        self.set_starter(starter)
        self.set_maincourse(maincourse)
        self.set_dessert(dessert)
            
    def set_starter(self, starter):
        self.starter = starter
        
    def set_maincourse(self,maincourse):
        self.maincourse = maincourse
        
    def set_dessert(self,dessert):
        self.dessert = dessert
        
    def get_starter(self):
        return self.starter
    
    def get_maincourse(self):
        return self.maincourse
    
    def get_dessert(self):
        return self.dessert
