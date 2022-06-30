'''
Created on 25 juin 2022

@author: Aurelien Giroux
'''
from food.Ingredient import Ingredient
class Ingredients(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        ingredients=[None,None,None,None,None]
        str_ingredients=['starters','accompaniments','meats','fishes','desserts']
        for i in range (5):
            file=open('dietery_recommendation/data/sorted_by_categories/'+str_ingredients[i]+'.csv','r')
            lines=file.read_lines()
            file.close()
            new_lines=[]
            for line in lines:
                new_lines.append(line.strip().split(';'))
            ingredients[i]=new_lines
        #self.ingredients_list = ingredients
        for ingredient_type in ingredients:
            for ingredient_param in ingredient_type:
                ingredient = Ingredient(ingredient_param)
                self.ingredients_list.append(ingredient)
        self.category_indexes_list = [[0],[1,2],[3,4],[5]]
        self.complexity_list = [[1.3,2.,1.4],[0.4,0.5,4.6,1.2],[0.39,0.35,0.8,1.8],[0.6,0.9,1.9],[0.7,2.3,3.1],[0.5,1.2]]
        
    total_meals=256301
    
    def get_type(self,target_ingredient):
        ''' Returns the type of an ingredient given in parameter '''
        for type in self.ingredients_list:
            for ingredient in type:
                if(ingredient == target_ingredient):
                    return type
        print("No such ingredient")
        return None
    
    def get_type_from_index(self,type_index):
        ''' Returns the type of the ingredient, given its index in the ingredients_list '''
        return self.ingredients_list[type_index]

    
    def get_type_index(self, target_ingredient):
        ''' Returns the index in the ingredients_list of the type of an ingredient given in parameter '''
        for i in range(len(self.ingredients_list)):
            for j in range(len(self.ingredients_list[i])):
                if(self.ingredients_list[i][j] == target_ingredient):
                    return i
        print("No such ingredient")
        return None
    
    def get_category_indexes(self,target_ingredient):
        ''' Returns the indexes in the ingredients_list of the types corresponding to the category of the ingredient given in the parameters '''
        type_index = self.get_type_index(self,target_ingredient)
        for category_indexes in self.category_indexes_list:
            if type_index in category_indexes:
                return category_indexes
        return None
    
    def get_information_ingredient(self,target_ingredient):
        '''Returns a list with all the information about target_ingredient'''
        for plate in self.ingredients:
            for ingredient in plate:
                if (target_ingredient==ingredient[3]):
                    return ingredient
                
    def get_average_consumption(self,ingredient):
        '''11000 approximately corresponds to the number of participants included in the inca3 study'''
        return ingredient.get_average_consumption(ingredient)
    
    def get_popularity_frequency(self,ingredient):
        '''256301 corresponds to the number of ingredients eaten during the inca3 study'''
        return ingredient.get_popularity_frequency(ingredient)
    
    
    # def get_complexity(self, target_ingredient):
    #     ''' Returns the complexity of an ingredient given in parameter '''
    #     ingredients_list = [["concombre","tomate","salade"],["pomme de terre","tomate","topinambour","epinards"],["riz","pates","pain","quiche"],["blancs de poulet","cote de porc", "gigot d'agneau"],["pave de saumon","dos de cabillaud", "steack de thon"],["yaourt","reblochon"]]
    #     category_indexes_list = [[0],[1,2],[3,4],[5]]
    #     complexity_list = [[1.3,2.,1.4],[0.4,0.5,4.6,1.2],[0.39,0.35,0.8,1.8],[0.6,0.9,1.9],[0.7,2.3,3.1],[0.5,1.2]]
    #
    #     i = self.get_type_index(self, target_ingredient)
    #     type = ingredients_list[i]
    
    #     j = -1
    #     for k in range(len(type)):
    #         if(type[k] == target_ingredient):
    #             j=k
    #             break
    #     score = complexity_list[i][j]
    
    #     #aliment_expected_complexity = Kolmogorov.Kolmogorov.kolmogorov_ingredient(Kolmogorov.Kolmogorov, target_ingredient, History.History)
    #     #aliment_observed_complexity = 
    #     #aliment_contraint_complexity = constraint.Constraint(constraint.Constraint
    #     #simplicity = aliment_expected_complexity - aliment_observed_complexity
    #     #score = simplicity + aliment_contraint_complexity
    #
    #     return score