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

        ingredients=[None,None,None,None,None]
        str_ingredients=['starters','accompaniments','meats','fishes','desserts']
        for i in range (5):
            file=open('dietery_recommendation/data/sorted_by_categories/'+str_ingredients[i]+'.csv','r')
            lines=file.read_lines()
            file.close()
            ingredients[i]=lines
        self.ingredients_list = ingredients
        self.category_indexes_list = [[0],[1,2],[3,4],[5]]
        self.complexity_list = [[1.3,2.,1.4],[0.4,0.5,4.6,1.2],[0.39,0.35,0.8,1.8],[0.6,0.9,1.9],[0.7,2.3,3.1],[0.5,1.2]]
        
    def get_type(self,target_ingredient):

        for type in self.ingredients_list:
        ''' Returns the type of an ingredient given in parameter '''

            for ingredient in type:
                if(ingredient == target_ingredient):
                    return type
        print("No such ingredient")
        return None
    
    def get_type_from_index(self,type_index):

        return self.ingredients_list[type_index]
        ''' Returns the type of the ingredient, given its index in the ingredients_list '''

    
    def get_type_index(self, target_ingredient):

        for i in range(len(self.ingredients_list)):
            for j in range(len(self.ingredients_list[i])):
                if(self.ingredients_list[i][j] == target_ingredient):
        ''' Returns the index in the ingredients_list of the type of an ingredient given in parameter '''

                    return i
        print("No such ingredient")
        return None
    
    def get_category_indexes(self,target_ingredient):

        type_index = self.get_type_index(self,target_ingredient)
        for category_indexes in self.category_indexes_list:
        ''' Returns the indexes in the ingredients_list of the types corresponding to the category of the ingredient given in the parameters '''

            if type_index in category_indexes:
                return category_indexes
        return None
    

    # def get_complexity(self, target_ingredient):
    #     i = self.get_type_index(self, target_ingredient)
    #     type = self.ingredients_list[i]
    #     j = -1
    #     for k in range(len(type)):
    #         if(type[k] == target_ingredient):
    #             j=k
    #             break
    #     return complexity_list[i][j]
    
    
