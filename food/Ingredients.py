'''
Created on 25 juin 2022

@author: Aurelien Giroux
'''

class Ingredients(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.ingredients_list = [["concombre","tomate","salade"],["pomme de terre","tomate","topinambour","epinards"],["riz","pates","pain","quiche"],["blancs de poulet","cote de porc", "gigot d'agneau"],["pave de saumon","dos de cabillaud", "steack de thon"],["yaourt","reblochon"]]
        self.category_indexes_list = [[1],[2,3],[4,5],[6]]
        
    def get_type(self,target_ingredient):
        for type in self.ingredients_list:
            for ingredient in type:
                if(ingredient.__eq__(target_ingredient)):
                    return type
        print("No such ingredient")
        return None
    
    def get_type_index(self, target_ingredient):
        ingredients_list = [["concombre","tomate","salade"],["pomme de terre","tomate","topinambour","epinards"],["riz","pates","pain","quiche"],["blancs de poulet","cote de porc", "gigot d'agneau"],["pave de saumon","dos de cabillaud", "steack de thon"],["yaourt","reblochon"]]
        for i in range(len(ingredients_list)):
            for j in range(len(ingredients_list[i])):
                if(ingredients_list[i][j].__eq__(target_ingredient)):
                    return i
        print("No such ingredient")
        return None
    
    def get_category_indexes(self,target_ingredient):
        category_indexes_list = [[1],[2,3],[4,5],[6]]
        type_index = self.get_type_index(self,target_ingredient)
        for category_indexes in category_indexes_list:
            if type_index in category_indexes:
                return category_indexes
        return None
        