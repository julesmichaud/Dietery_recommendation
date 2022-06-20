'''
Created on Jun 20, 2022

@author: valerio
'''

class Repas:
    '''
    classdocs
    '''


    def __init__(self, entree, plat, dessert):
        '''
        Constructor
        '''
        self.set_entree(entree)
        self.set_plat(plat)
        self.set_dessert(dessert)
            
    def set_entree(self,entree):
        self.entree = entree
        
    def set_plat(self,plat):
        self.plat = plat
        
    def set_dessert(self,dessert):
        self.dessert = dessert
        
    def get_entree(self):
        return self.entree
    
    def get_plat(self):
        return self.plat
    
    def get_dessert(self):
        return self.dessert
 