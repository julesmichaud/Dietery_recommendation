'''
Created on 21 juin 2022

@author: dardare
'''

class environment(object):
    '''
    classdocs
    '''


    def __init__(self, date,promotions):
        '''
        Constructor
        '''
        self.set_date(date) #A string giving the current date 
        self.set_promotions(promotions) #a dictionnary giving Ingredient and market ans promotion associate
        
        
    def set_date(self,date):
        self.date = date
        
    def set_discount(self,promotions):
        self.promotions= promotions
        
    def get_date(self):
        return self.date
    
    def get_promotion(self):
        return self.promotion
    
    def add_ingredient(self,ingredient):
        self.promotions[ingredient]={}
        
    def add_promotion(self,market,promotion,ingredient): #Add promotion (0 to 1) at ingredient of market 
        promo_ingredient = self.promotion[ingredient]
        promo_ingredient[market]=promotion
        self.promotion[ingredient]=promo_ingredient
        
        
        
    