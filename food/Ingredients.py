'''
Created on 25 juin 2022

@author: Aurelien Giroux
'''
from gevent.libev.corecext import type

class Ingredients(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.ingredients_list = [["concombre","tomate","salade"],["pomme de terre","tomate","topinambour","épinards"],["riz","pâtes","pain","quiche"],["blancs de poulet","côte de porc", "gigot d'agneau"],["pavé de saumon","dos de cabillaud", "steack de thon"],["yaourt","reblochon"]]
        category_indexes_list = [[1],[2,3],[4,5],[6]]
        
    def get_type(self,target_ingredient):
        for type in self.ingredients_list:
            for ingredient in type:
                if(ingredient.__eq__(target_ingredient)):
                    return type
        print("No such ingredient")
        return None
    
    def get_type_index(self, target_ingredient):
        for i in range(len(self.ingredients_list)):
            for j in range(len(self.ingredients_list[i])):
                if(self.ingredients_list[i][j].__eq__(target_ingredient)):
                    return i
        print("No such ingredient")
        return None
    
    def get_category_indexes(self,target_ingredient):
        type_index = self.get_type_index(target_ingredient)
        for category_indexes in self.category_indexes_list:
            if type_index in category_indexes:
                return category_indexes
        return None
        