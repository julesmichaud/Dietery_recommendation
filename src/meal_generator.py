'''
Created on 22 juin 2022

@author: Aurelien Giroux
'''
from food.alimentary_sequence import Alimentary_sequence
from food import Ingredients
import random
from kolmogorov import Kolmogorov
from user import History

class Meal_generator(object):
    '''
    Generates one meal, based on the user profile at an instant
    '''
    
    def __init__(self,user,ingredients):
        '''
        Stores the user profile and the ingredients with which the generator will generate meals. We also set a constant which will determine the threshold at which we will print a sentence to the user about the surprising selection of an ingredient
        '''
        self.user = user
        self.ingredients = ingredients
        self.detection_threshold = 3
        
    def smallest_out_of_two(self,nbr1, nbr2):
        ''' Returns the smallest number out of the two seized '''
        if(nbr1<nbr2):
            return nbr1
        return nbr2
    
    def explore_type(self,type, n): #type is a list of ingredients
        ''' Returns the least complex ingredient out of all of those present in a type '''
        explored_ingredient_indexes = []
        least_complex_ingredient = "Giberish"
        min_complexity = 9999999
        for i in range(n): #We explore n ingredients whithin each type
            ingredient_index = random.randint(0,len(type)-1)
            while(ingredient_index in explored_ingredient_indexes):
                ingredient_index = random.randint(0,len(type)-1)
            ingredient = type[ingredient_index]
            explored_ingredient_indexes.append(ingredient_index)
            current_complexity = Kolmogorov.Kolmogorov.kolmogorov_ingredient(Kolmogorov.Kolmogorov, self.user, self.ingredients, ingredient)#, History.History)
            if(current_complexity<min_complexity):
                min_complexity = current_complexity
                least_complex_ingredient = ingredient
        return least_complex_ingredient
    
    def select_neighbors(self,ingredient, k, n):
        ''' Returns the least complex ingredients present in each type of the category of the input ingredient '''
        #category_indexes = Ingredients.Ingredients.get_category_indexes(self.ingredients,ingredient) #We get the indexes of the category of the aliment
        category_indexes = self.ingredients.get_category_indexes(ingredient) #We get the indexes of the category of the aliment
        #type_index = Ingredients.Ingredients.get_type_index(self.ingredients,ingredient) #We get the index of the type whithin the category
        type_index = self.ingredients.get_type_index(ingredient) #We get the index of the type whithin the category
        
        explored_category_indexes = [type_index]
        #type = Ingredients.Ingredients.get_type(self.ingredients,ingredient)
        type = self.ingredients.get_type(ingredient)
        n_type = self.smallest_out_of_two(n, len(type))
        least_complex_list = [self.explore_type(type,n_type)]
        
        k = self.smallest_out_of_two(self,k, len(category_indexes))
        
        for i in range(k-1): #We explore k neighboring types within the category, and n ingredients whithin each type
            type_index = random.randint(category_indexes[0],category_indexes[-1])
            while(type_index in explored_category_indexes):
                type_index = random.randint(category_indexes[0],category_indexes[-1])
                
            explored_category_indexes.append(type_index)
            #type = Ingredients.Ingredients.get_type_from_index(self.ingredients,type_index)
            type = self.ingredients.get_type_from_index(type_index)
            n_type = self.smallest_out_of_two(self,n, len(type))
            least_complex_list.append(self.explore_type(self,type,n_type))
            
        return least_complex_list
    
    def select_neighbor(self,least_complex_list):
        ''' Returns the least complex ingredient out of all the ingredients of a list '''
        min_ingredient = least_complex_list[0]
        min_complexity = Kolmogorov.Kolmogorov.kolmogorov_ingredient(self, min_ingredient)
        for ingredient in least_complex_list:
            complexity = Kolmogorov.Kolmogorov.kolmogorov_ingredient(self, ingredient)
            if(complexity<min_complexity):
                min_complexity = complexity
                min_ingredient = ingredient
        return min_ingredient
    
    def generate_ingredient(self,source_ingredient, k, n):
        ''' Based on a source ingredient, returns the least complex ingredient of its category '''
        selected_ingredient = self.select_neighbor(self.select_neighbors(source_ingredient, k, n)) 
        return selected_ingredient
        
    def generate_meal(self, ingredients):
        ''' Generates a brand new full meal '''
        time = 0
        for i in range(len(ingredients)):
            ingredients[i]=self.generate_ingredient(ingredients[i],2,2)
        sequence = Alimentary_sequence(ingredients, time)
        print("\n")
        print(sequence)
        print("\n")
        return sequence
    
    def explain_meal(self,origin_sequence, generated_sequence):
        ''' Explains the choice of a meal (the generated_sequence), when compared to another (the origin_sequence) '''
        for i in range(len(origin_sequence)):
            #Before anything, get a hold of the intermediate values for the calculation of each of the meals' complexities, and compare them
            #We can get information by comparing the different factors of complexity, as well as with somewhat arbitrary thresholds for things like the rarity of a product
            if(origin_sequence[i][3]==generated_sequence[i][3]):
                print("Comme vous avez semble beaucoup aimer " + origin_sequence[i][3] + ", nous vous l'avons repropose.")
            else:
                print("Pour changer de " + origin_sequence[i][3] + ", nous vous avons propose plutot " + generated_sequence[i] + ".")
            
            original_complixity_factors = Kolmogorov.Kolmogorov.explainable_kolmogorov_ingredient(Kolmogorov.Kolmogorov, origin_sequence[i][3], History.History)
            generated_complixity_factors = Kolmogorov.Kolmogorov.explainable_kolmogorov_ingredient(Kolmogorov.Kolmogorov, generated_sequence[i][3], History.History)
            for j in range(len(original_complixity_factors)):
                current_difference = generated_complixity_factors[j][3] - original_complixity_factors[j][3]
                if(current_difference>self.detection_threshold): #Change deemed significant regarding specific aspect
                    if(j==0): #Surprise over availability period of the ingredient
                        #print(""+ str(generated_sequence[i][3]) + " n'est disponible que " + Ingredients.Ingredients.get_availability_period(ingredients,generated_sequence[i][3]) + "jours cette annee, et c'est pourquoi nous vous l'avons propose")
                        print(""+ str(generated_sequence[i][3]) + " n'est disponible que " + self.ingredients.get_availability_period(generated_sequence[i][3]) + "jours cette annee, et c'est pourquoi nous vous l'avons propose")
                    if(j==1): #Surprise over overall popularity of the ingredient
                        print("Pour vous surprendre au quotidien, nous avons souhaite vous proposer un aliment rarement present dans la diete des francais :" + str(generated_sequence[i][3]))
                #if(current_difference<-2):
            
