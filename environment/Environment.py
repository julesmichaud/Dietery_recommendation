'''
Created on 21 juin 2022

@author: Clement Dardare
'''

class environment(object):
    '''
    This class contains elements that depend on the environment of the person and that could influence its eating habits. For the moment, this class has no use in the rest of our program
    '''

    def __init__(self, date,promotions):
        '''
        We set up different parameters of the envrionment
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
        