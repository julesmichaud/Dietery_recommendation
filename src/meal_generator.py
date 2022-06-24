'''
Created on 22 juin 2022

@author: Aurelien Giroux
'''
from food.alimentary_sequence import Alimentary_sequence
import ingredients #new class, which has all aliments listed by categories under the form of a list of lists : a list is a category, which contains lists that represent types
import random
from kolmogorov import Kolmogorov
from user import History

def explore_type(type, n): #type is a list of ingredients
    explored_ingredient_indexes = []
    least_complex_couple = [None,None]
    min_complexity = 9999999
    for i in range(n): #We explore n ingredients whithin each type
        ingredient_index = random.randint(0,type.size())
        while(ingredient_index in explored_ingredient_indexes):
            ingredient_index = random.randint(0,type.size())
        ingredient = type[ingredient_index]
        explored_ingredient_indexes.append(ingredient_index)
        current_complexity = Kolmogorov.Kolmogorov.kolmogorov_ingredient(Kolmogorov.Kolmogorov, ingredient, History.History)
        if(current_complexity<min_complexity):
            min_complexity = current_complexity
            least_complex_couple[0]=min_complexity
            least_complex_couple[1]=ingredient
    return least_complex_couple

def select_neighbours(ingredient, k, n):
    category_index = ingredients.get_category_index(ingredient) #We get the index of the category of the aliment
    type_index = ingredients.get_type_index(category_index,ingredient) #We get the index of the type whithin the category
    explored_category_indexes = [type_index]
    least_complex_list = [explore_type(category_index,type_index)]
    
    for i in range(k-1): #We explore k neighboring types within the category, and n ingredients whithin each type
        type_index = random.randint(0,ingredients.get_set_of_categories_size())
        while(type_index in explored_types_indexes):
            category_index = random.randint(0,ingredients.get_set_of_categories_size())
        explored_types_indexes.append(type_index)
        type = ingredients.get_type(type_index)
        least_complex_list.append(explore_type(type,n))
    return least_complex_list #format : a list of lists : these lists contain the complexity of the ingredient, and the ingredient

def select_neighbour(least_complex_list):
    min_complexity = least_complex_list[0][0]
    min_ingredient = least_complex_list[0][1]
    for couple in least_complex_list:
        complexity = couple[0]
        if(complexity<min_complexity):
            min_complexity = complexity
            min_ingredient = couple[1]
    return min_ingredient

def generate_meal(number_of_menus):
    ingredients = [] #To initialize with the ingredients of the last meal
    time = 0
    print("Generating " + str(number_of_menus) + " menus...")
    sequence = Alimentary_sequence(ingredients, time)
    print("Done ! Here you go ;)")
    print(sequence)

if __name__ == '__main__':
    generate_meal()