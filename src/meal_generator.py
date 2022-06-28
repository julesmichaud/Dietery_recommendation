'''
Created on 22 juin 2022

@author: Aurelien Giroux
'''
from food.alimentary_sequence import Alimentary_sequence
from food import Ingredients #new class, which has all aliments listed by categories under the form of a list of lists : a list is a category, which contains lists that represent types
import random
from kolmogorov import Kolmogorov
from user import History

ingredients = Ingredients.Ingredients

class Meal_generator(object):
    
    def smallest_out_of_two(self,nbr1, nbr2):
        if(nbr1<nbr2):
            return nbr1
        return nbr2
    
    def explore_type(self,type, n): #type is a list of ingredients
        explored_ingredient_indexes = []
        #least_complex_couple = [None,None]
        least_complex_ingredient = "Giberish"
        min_complexity = 9999999
        for i in range(n): #We explore n ingredients whithin each type
            ingredient_index = random.randint(0,len(type)-1)
            while(ingredient_index in explored_ingredient_indexes):
                ingredient_index = random.randint(0,len(type)-1)
            ingredient = type[ingredient_index]
            explored_ingredient_indexes.append(ingredient_index)
            #current_complexity = Kolmogorov.Kolmogorov.kolmogorov_ingredient(Kolmogorov.Kolmogorov, ingredient, History.History)
            current_complexity = ingredients.get_complexity(ingredients, ingredient)
            if(current_complexity<min_complexity):
                min_complexity = current_complexity
                #least_complex_couple[0]=min_complexity
                #least_complex_couple[1]=ingredient
                least_complex_ingredient = ingredient
        return least_complex_ingredient
    
    def select_neighbors(self,ingredient, k, n):
        category_indexes = ingredients.get_category_indexes(ingredients,ingredient) #We get the indexes of the category of the aliment
        type_index = ingredients.get_type_index(ingredients,ingredient) #We get the index of the type whithin the category
        
        
        explored_category_indexes = [type_index]
        type = ingredients.get_type(ingredients,ingredient)
        n_type = self.smallest_out_of_two(self,n, len(type))
        least_complex_list = [self.explore_type(self,type,n_type)]
        
        k = self.smallest_out_of_two(self,k, len(category_indexes))
        
        for i in range(k-1): #We explore k neighboring types within the category, and n ingredients whithin each type
            type_index = random.randint(category_indexes[0],category_indexes[-1])
            while(type_index in explored_category_indexes):
                type_index = random.randint(category_indexes[0],category_indexes[-1])
                
            explored_category_indexes.append(type_index)
            type = ingredients.get_type_from_index(ingredients,type_index)
            n_type = self.smallest_out_of_two(self,n, len(type))
            least_complex_list.append(self.explore_type(self,type,n_type))
            
        return least_complex_list
    
    def select_neighbor(self,least_complex_list):
        min_ingredient = least_complex_list[0]
        min_complexity = ingredients.get_complexity(ingredients, min_ingredient)
        for ingredient in least_complex_list:
            complexity = ingredients.get_complexity(ingredients, ingredient)
            if(complexity<min_complexity):
                min_complexity = complexity
                min_ingredient = ingredient
        return min_ingredient
    
    def generate_ingredient(self,source_ingredient, k, n):
        selected_ingredient = self.select_neighbor(self,self.select_neighbors(self,source_ingredient, k, n)) 
        return selected_ingredient
        
    def generate_meal(self):
        ingredients = ["salade","pave de saumon", "epinards", "yaourt"] #To initialize with the ingredients of the last meal from History
        #ingredients = History.History.get_meals(History.History)[-1]
        time = 0
        for i in range(len(ingredients)):
            ingredients[i]=self.generate_ingredient(self,ingredients[i],2,2)
        sequence = Alimentary_sequence(ingredients, time)
        print("\n")
        print(sequence)
        print("\n")
        return sequence
    
    def explain_meal(self,origin_sequence, generated_sequence):
        for i in range(len(origin_sequence)):
            #Before anything, get a hold of the intermediate values for the calculation of each of the meals' complexities, and compare them
            #We can get information by comparing the different factors of complexity, as well as with somewhat arbitrary thresholds for things like the rarity of a product
            if(origin_sequence[i]==generated_sequence[i]):
                print("Comme vous avez semble beaucoup aimer " + origin_sequence[i] + ", nous vous l'avons repropose.")
            else:
                print("Pour changer de " + origin_sequence[i] + ", nous vous avons propose plutot " + generated_sequence[i] + ".")
            original_complixity_factors = Kolmogorov.Kolmogorov.explainable_kolmogorov_ingredient(Kolmogorov.Kolmogorov, origin_sequence[i], History.History)
            generated_complixity_factors = Kolmogorov.Kolmogorov.explainable_kolmogorov_ingredient(Kolmogorov.Kolmogorov, generated_sequence[i], History.History)
            for j in range(len(original_complixity_factors)):
                current_difference = generated_complixity_factors[j] - original_complixity_factors[j]
                if(current_difference>2): #Change deemed significant regarding specific aspect
                    if(j==0): #Surprise sur la période de disponibilité
                        print(""+ str(generated_sequence[i]) + " n'est disponible que " + ingredients.get_availability_period(generated_sequence[i]) + "jours cette année")