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
        ingredients_list = [["concombre","tomate","salade"],["pomme de terre","tomate","topinambour","epinards"],["riz","pates","pain","quiche"],["blancs de poulet","cote de porc", "gigot d'agneau"],["pave de saumon","dos de cabillaud", "steack de thon"],["yaourt","reblochon"]]
        for type in ingredients_list:
            for ingredient in type:
                if(ingredient == target_ingredient):
                    return type
        print("No such ingredient")
        return None
    
    def get_type_from_index(self,type_index):
        ingredients_list = [["concombre","tomate","salade"],["pomme de terre","tomate","topinambour","epinards"],["riz","pates","pain","quiche"],["blancs de poulet","cote de porc", "gigot d'agneau"],["pave de saumon","dos de cabillaud", "steack de thon"],["yaourt","reblochon"]]
        return ingredients_list[type_index]
    
    def get_type_index(self, target_ingredient):
        ingredients_list = [["concombre","tomate","salade"],["pomme de terre","tomate","topinambour","epinards"],["riz","pates","pain","quiche"],["blancs de poulet","cote de porc", "gigot d'agneau"],["pave de saumon","dos de cabillaud", "steack de thon"],["yaourt","reblochon"]]
        for i in range(len(ingredients_list)):
            for j in range(len(ingredients_list[i])):
                if(ingredients_list[i][j] == target_ingredient):
                    return i
        print("No such ingredient")
        return None
    
    def get_category_indexes(self,target_ingredient):
        category_indexes_list = [[0],[1,2],[3,4],[5]]
        type_index = self.get_type_index(self,target_ingredient)
        for category_indexes in category_indexes_list:
            if type_index in category_indexes:
                return category_indexes
        return None
    
    def get_complexity(self, target_ingredient):
        ingredients_list = [["concombre","tomate","salade"],["pomme de terre","tomate","topinambour","epinards"],["riz","pates","pain","quiche"],["blancs de poulet","cote de porc", "gigot d'agneau"],["pave de saumon","dos de cabillaud", "steack de thon"],["yaourt","reblochon"]]
        category_indexes_list = [[0],[1,2],[3,4],[5]]
        complexity_list = [[1.3,2.,1.4],[0.4,0.5,4.6,1.2],[0.39,0.35,0.8,1.8],[0.6,0.9,1.9],[0.7,2.3,3.1],[0.5,1.2]]
        i = self.get_type_index(self, target_ingredient)
        type = ingredients_list[i]
        j = -1
        for k in range(len(type)):
            if(type[k] == target_ingredient):
                j=k
                break
        return complexity_list[i][j]