'''
Created on 22 juin 2022

@author: Aurelien Giroux
'''
#The main needs to do the following :
# - Take as an input whether the user wants to configure the program or if it wants to generate menus
#    - If it wants configurations, ask the user what parameters he wants to change, and direct him to the appropriate menu of the program
#    - If it wants to generate menus, ask how many the user wants
# - After being done with a menu, always redirect to the previous menu. Always offer a "go back" option
from click._compat import raw_input
from src import meal_generator
from food.alimentary_sequence import Alimentary_sequence
from user.User import User
from food.Ingredient import Ingredient
from food.Ingredients import Ingredients
from copy import deepcopy

def initialisation():
    ''' We initialize the ingredients, as well as the user profile with a "selection" of meals for 2 weeks '''
    all_params=[['14', '4342', 'flan sale', 'quiche sans pate', 'salty flan', '18', '18', '182', '182', '', '', '', '', '', '', '', '6F,7E,P4,L4,O6,G4', '', '', '', '03', '', '', '', '', '', '', 'A03YJ#F04.A036P$F04.A02LT$F04.A02NC$F04.A031F$F04.A00SB$F04.A025C$F04.A02YP$F04.A00HF$F22.A07SS', 'Egg based dishes, Home prepared (family, social networks, proxies),Olive oils,Milk,Creme fraiche and other mild variants of sour cream,Whole eggs,Leeks,Chorizo and similar,Cheese, gruyere,Shallots', 'A03VA', 'Composite dishes', 'A03VB', 'Dishes, incl. Ready to eat meals (excluding soups and salads)', 'A03VC', 'Dishes excluding pasta or rice dishes, sandwiches and pizza)', '40'], ['14', '1077', 'oeuf n.s.', '', 'egg n.s.', '9', '9', '91', '91', '', '', '07', '', '34', '', '', '', '', '', '', '', '', '', '', '00', '01', '', 'A031F#F01.A057Z$F21.A0C6S$F28.A07GY', 'Whole eggs, Gallus gallus (live animals),Back yard farming - growing,Roasting', 'A031E', 'Eggs and egg products', 'A04NY', 'Unprocessed eggs', 'A031F', 'Whole eggs', '13'], ['38', '2601', 'beignet sale de legumes', '', 'vegetables, fritter', '2', '2', '20', '20', '', '', '', '', '09', '', '', 'M2,FF', '', '', '', '03', '', '', '', '', '01', '', 'A03XX#F04.A00AJ$F04.A00JR$F04.A0DGR$F21.A0C6S$F22.A07SS$F26.A07XE$F28.A07GS', 'Vegetable based dishes, Home prepared (family, social networks, proxies),Other,Beignets,Courgettes,Courgette (edible flowers),Back yard farming - growing,Pan frying / shallow frying', 'A03VA', 'Composite dishes', 'A03VB', 'Dishes, incl. Ready to eat meals (excluding soups and salads)', 'A03VC', 'Dishes excluding pasta or rice dishes, sandwiches and pizza)', '23'], ['38', '9405', 'celeri remoulade', '', 'celery remoulade', '23', '23', '234', '234', '', '', '', '', '', '00', '', '', '', '', '', '22', '', '', '', '', '', '', 'A042B#F04.A00QJ$F04.A044X$F22.A07SQ', 'Salads, Canteen / localized catering prepared,Celeriacs,Mayonnaise sauce', 'A03VA', 'Composite dishes', 'A041K', 'Soups and salads', 'A042B', 'Salads', '49'], ['38', '3375', 'melange de legumes pour potage', '', 'vegetables, mixed for soup', '2', '2', '20', '20', '', '', '', '', '94', '00', '', '00', '', '', '', '22', '', '', '', '', '', '', 'A03XX#F22.A07SQ$F28.A0BA1', 'Vegetable based dishes, Canteen / localized catering prepared,Cooking and similar thermal preparation processes', 'A03VA', 'Composite dishes', 'A03VB', 'Dishes, incl. Ready to eat meals (excluding soups and salads)', 'A03VC', 'Dishes excluding pasta or rice dishes, sandwiches and pizza)', '16'], ['21', '69', 'chou fleur', '', 'cauliflower', '2', '2', '24', '24', '', '', '', '', '09', '17', '', '', '', '', '', '', '', '', '', '', '03', '99', 'A00FR#F26.A07XE$F28.A07GS$F28.A07KP', 'Cauliflowers, Other,Pan frying / shallow frying,Chilling', 'A00FJ', 'Vegetables and vegetable products', 'A00FL', 'Flowering brassica', 'A0DLL', 'Cauliflowers and similar-', '184'], ['5', '2227', 'pate alimentaire au ble complet', '', 'pasta, wheat, wholemeal', '6', '6', '62', '62', '', '', '', '', '03', '01', '99', '', '', '', '', '06', '', '', '', '', '', '99', 'A04LC#F06.A0BA5$F22.A07SH$F28.A07GL$F28.A0BYP', 'Pasta wholemeal, Food industry prepared,In air (normal atmosphere),Boiling,Canning / jarring', 'A000J', 'Grains and grain-based products', 'A04QT', 'Pasta, doughs and similar products', 'A007D', 'Pasta and similar products', '79'], ['4', '5056', 'melange de cereales (semoule de ble et semoule de mais)', '', 'wheat and mais semolina', '6', '6', '62', '62', '', '', '', '', '03', '18', '', '', '', '', '', '', '', '', '', '', '', '99', 'A0ETL#F27.A002N$F27.A004F$F28.A07GL$F28.A07KG', 'Semolina, Maize semolina,Wheat semolina,Boiling,Drying (dehydration)', 'A000J', 'Grains and grain-based products', 'A000K', 'Cereals and cereal primary derivatives', 'A0ETL', 'Semolina', '1'], ['23', '13', 'topinambour', 'artichaut de jerusalem, truffe du canada, poire de terre', 'artichoke, jerusalem', '1', '1', '10', '10', '', '', '', '16', '44', '', '', '', '', '', '', '', '', '', '', '', '01', '', 'A00QQ#F03.A06JB$F21.A0C6S$F28.A07GQ', 'Jerusalem artichokes, Dices / sticks,Back yard farming - growing,Pressure cooking', 'A00FJ', 'Vegetables and vegetable products', 'A00QF', 'Root and tuber vegetables (excluding starchy- and sugar-)', 'A0DNV', 'Jerusalem artichokes and similar-', '9'], ['21', '19', 'salade epinard', 'epinard', 'spinach', '2', '2', '21', '21', '', '', '', '', '32', '02', '', '', '', '', '', '', '', '', '', '', '03', '02', 'A00MJ#F28.A07HB$F28.A07KQ', 'Spinaches, Microwave-cooking,Freezing', 'A00FJ', 'Vegetables and vegetable products', 'A00KR', 'Leafy vegetables', 'A00MG', 'Spinach-type leaves', '193'], ['19', '1030', 'calamar', 'encornet, chipiron, supion', 'squids', '8', '8', '82', '82', '821', '821', '', '', '52', '02', '', '', '', '', '', '', '', '', '', '', '00', '', 'A02JH#F28.A07GV$F28.A07HK$F28.A07KQ', 'Squids, Deep frying,Breading,Freezing', 'A026T', 'Fish, seafood, amphibians, reptiles and invertebrates', 'A02GM', 'Molluscs', 'A02HZ', 'Squids, cuttlefishes, octopuses', '36'], ['18', '3293', 'lamproie', '', 'lamprey', '8', '8', '81', '81', '811', '811', '', '16', '40', '01', '00', '', '', '', '06', '', '01', '', '', '02,05', '03', '03', 'A0EYR#F03.A06JB$F17.A07MZ$F19.A07PF$F20.A07QR$F26.A07XE$F27.A026X$F28.A07GM$F28.A07KP', 'Canned/jarred fish, Dices / sticks,Other,Outside brown,Glass,W/o skin,Freshwater fish,Stewing,Chilling', 'A026T', 'Fish, seafood, amphibians, reptiles and invertebrates', 'A04NL', 'Fish and seafood processed', 'A02KB', 'Processed or preserved fish (including processed offals)', '1'], ['17', '5088', 'jambon en croute', '', 'jambon en croute', '7', '7', '74', '74', '741', '741', '05', '', '', '17,10', '', '', '', '', '05', '', '', '', '', '', '', '03', 'A03VV#F04.A022T$F04.A00BT$F19.A07PR$F28.A07KP$F28.A07JK', 'Meat based dishes, Ham, pork,Brioche type products,Plastic,Chilling,Vacuum-packing', 'A03VA', 'Composite dishes', 'A03VB', 'Dishes, incl. Ready to eat meals (excluding soups and salads)', 'A03VC', 'Dishes excluding pasta or rice dishes, sandwiches and pizza)', '1'], ['15', '1888', 'brochette de porc', '', 'pork, skewer', '7', '7', '71', '71', '713', '713', '05', '', '43', '00', '', '', '', '', '00', '', '', '', '', '02,05', '', '00', 'A01RG#F17.A07MV$F17.A07MZ$F26.A07XE$F28.A07GS', 'Pig muscle, Other,Meat inside "medium",Outside brown,Pan frying / shallow frying', 'A01QR', 'Meat and meat products', 'A0EYH', 'Mammals and birds meat', 'A0EYF', 'Mammals meat', '9'], ['16', '2835', 'haut de cuisse de canard', '', 'duck, leg, high', '7', '7', '72', '72', '723', '723', '08', '', '94', '00', '', '', '', '', '06', '', '01', '', '', '03,06', '03', '00', 'A01SR#F02.A07XQ$F17.A07MX$F17.A07NA$F19.A07PF$F20.A07QR$F26.A07XE$F28.A0BA1', 'Duck fresh meat, Leg (as part-nature),Other,Meat inside " well done",Outside dark brown/slightly burned,Glass,W/o skin,Cooking and similar thermal preparation processes', 'A01QR', 'Meat and meat products', 'A0EYH', 'Mammals and birds meat', 'A0EYG', 'Birds meat', '2'], ['25', '122', 'abricot (frais)', '', 'apricot', '4', '4', '41', '41', '413', '413', '', '', '34', '01', '17', '', '', '', '04', '', '', '', '', '', '03', '99', 'A01NS#F06.A06XZ$F19.A07PG$F28.A07GY', 'Canned or jarred apricot, In diluted sweet liquid-syrup,Metal,Roasting', 'A01BS', 'Fruit and fruit products', 'A01ML', 'Processed fruit products', 'A01QD', 'Other processed fruit products (excluding beverages)', '2'], ['27', '1189', 'barre chocolatee type snickers', 'snickers (barre chocolatee)', 'chocolate bar like snickers', '11', '11', '112', '112', '1122', '1122', '', '', '', '', '', '01', '', '', '', '', '', '', '', '', '', '', 'A0EQR#F04.A015H$F04.A035A$F28.A07HP', 'Sweet bars and other formed sweet masses, Peanuts,Caramel, soft,Chocolate coating', 'A032F', 'Sugar and similar, confectionery and water-based sweet desserts', 'A04PE', 'Confectionery including chocolate', 'A0EQR', 'Sweet bars and other formed sweet masses', '28'], ['27', '3753', "riz souffle enrobe de chocolat type m&m's crispy", "m&m's crispy (riz souffle)", "m&m's, rice", '11', '11', '112', '112', '1124', '1124', '', '', '', '', '', '01', '', '', '05', '', '', '', '', '', '', '', 'A035F#F04.A00DR$F04.A0EQD$F19.A07PR', 'Dragee, sugar coated, Rice, popped,Chocolate and similar,Plastic', 'A032F', 'Sugar and similar, confectionery and water-based sweet desserts', 'A04PE', 'Confectionery including chocolate', 'A0EQQ', 'Candies (soft and hard)', '4'], ['6', '2711', 'biscuit dietetique fourre', '', 'cookie diet filled chocolate', '12', '12', '122', '122', '1222', '1222', '', '', '', '', '', '', '00', '00', '05', '06', '', '', '', '', '', '', 'A00AE#F19.A07PR$F23.A07TP$F28.A07MA', 'Biscuit with inclusions, filling or coating, Plastic,Special diets,Filling', 'A000J', 'Grains and grain-based products', 'A009T', 'Fine bakery wares', 'A009V', 'Biscuits', '1'], ['9', '3434', 'munster n.s.', '', 'munster n.s.', '5', '5', '55', '55', '551', '551', '02', '', '', '', '', '', '', '', '05', '', '', '', '', '', '', '', 'A02RN#F19.A07PR', 'Cheese, munster, Plastic', 'A02LR', 'Milk and dairy products', 'A02QE', 'Cheese', 'A02RG', 'Ripened cheese', '6']]
    entrees = [Ingredient(all_params[0]),Ingredient(all_params[1]),Ingredient(all_params[2]),Ingredient(all_params[3]),Ingredient(all_params[4])]
    plats = [Ingredient(all_params[5]),Ingredient(all_params[6]),Ingredient(all_params[7]),Ingredient(all_params[8]),Ingredient(all_params[9])]
    accompagnements = [Ingredient(all_params[10]),Ingredient(all_params[11]),Ingredient(all_params[12]),Ingredient(all_params[13]),Ingredient(all_params[14])]
    desserts = [Ingredient(all_params[15]),Ingredient(all_params[16]),Ingredient(all_params[17]),Ingredient(all_params[18]),Ingredient(all_params[19])]

    to_init_list = [Alimentary_sequence([entrees[0],plats[0],accompagnements[0],desserts[0]], 0)] #1
    to_init_list.append(Alimentary_sequence([entrees[1],plats[0],accompagnements[1],desserts[0]], 0)) #2
    to_init_list.append(Alimentary_sequence([entrees[0],plats[1],accompagnements[1],desserts[2]], 0)) #3
    to_init_list.append(Alimentary_sequence([entrees[2],plats[1],accompagnements[0],desserts[1]], 0)) #4
    to_init_list.append(Alimentary_sequence([entrees[3],plats[2],accompagnements[2],desserts[2]], 0)) #5
    to_init_list.append(Alimentary_sequence([entrees[1],plats[3],accompagnements[3],desserts[3]], 0)) #6
    to_init_list.append(Alimentary_sequence([entrees[4],plats[0],accompagnements[2],desserts[4]], 0)) #7
    to_init_list.append(Alimentary_sequence([entrees[2],plats[0],accompagnements[0],desserts[1]], 0)) #8
    to_init_list.append(Alimentary_sequence([entrees[4],plats[3],accompagnements[4],desserts[3]], 0)) #9
    to_init_list.append(Alimentary_sequence([entrees[3],plats[2],accompagnements[4],desserts[2]], 0)) #10
    to_init_list.append(Alimentary_sequence([entrees[0],plats[4],accompagnements[2],desserts[2]], 0)) #11
    to_init_list.append(Alimentary_sequence([entrees[0],plats[4],accompagnements[3],desserts[0]], 0)) #12
    to_init_list.append(Alimentary_sequence([entrees[1],plats[0],accompagnements[3],desserts[0]], 0)) #13
    to_init_list.append(Alimentary_sequence([entrees[1],plats[2],accompagnements[1],desserts[3]], 0)) #14
    
    #for meal in to_init_list:
    #    User.store_user_meal(User,meal)
        
    user = User(to_init_list, [4, True])
    ingredients = Ingredients()
    return user, ingredients

def is_back(user_in):
    ''' Checks if the user input said to go back a step in the program '''
    str.lower(user_in)
    if(user_in.__eq__("back")):
        return True
    return False

def is_exit(user_in):
    ''' Checks if the user input said to exit the program '''
    str.lower(user_in)
    if(user_in.__eq__("exit")):
        return True
    return False

def meal_arg_input():
    ''' Takes and checks the user input when we ask to input a menu '''
    number_str = raw_input("Please indicate how many menus you would like to generate\n")
    if(is_exit(number_str)):
        quit()
    if(is_back(number_str)):
        back_input_after_2()
        quit()
    try:
        number_int = int(number_str)
    except:
        print("Please type a number or command")
        number_int = meal_arg_input()
    if(number_int<=0):
        print("Please enter a strictly positive number")
        number_int = meal_arg_input()
    return number_int
    
def get_number_of_menus():
    ''' Returns the number of menus selected by the user, used to communicate this information to the meal_generator '''
    return number_of_menus

def back_input_after_2(user, generator):
    ''' Function called when the user types "back" after selecting the option "2" in the user menu '''
    user_in = raw_input("Type '1' to change your parameters and '2' to generate a meal. At any moment, type 'back' to go back and 'exit' to exit\n")
    if(is_back(user_in) or is_exit(user_in)):
        print("See you soon !")
        quit()
    elif(user_in.__eq__("1")):
        print("Temporary menu placeholder")
        quit()
        #Find a way to execute the general_menu file...
    elif(user_in.__eq__("2")):
        number_of_menus = meal_arg_input() #Also considers "back" and "exit"
        origin_sequence = user.get_last_user_meal()
        print("Generating " + str(number_of_menus) + " menu(s)...\n")
        for i in range(number_of_menus):
            true_origin_sequence = deepcopy(origin_sequence)
            generated_sequence = generator.generate_meal(origin_sequence.get_ingredients())
            generator.explain_meal(true_origin_sequence.get_ingredients(), generated_sequence.get_ingredients())
            origin_sequence = generated_sequence
            user.store_user_meal(generated_sequence)
        print("Done ! Here you go ;)\n")
        quit()
    else:
        print("Unrecognized input, please try again")
        back_input_after_2();
        quit()

if __name__ == '__main__':
    number_of_menus = 0
    user, ingredients = initialisation()
    generator = meal_generator.Meal_generator(user,ingredients)
    
    print("Welcome ! Would you like to modify your personal parameters or to generate a meal ?");
    
    user_in = raw_input("Type '1' to change your parameters and '2' to generate a meal. At any moment, type 'back' to go back and 'exit' to exit\n")
    if(is_back(user_in) or is_exit(user_in)):
        print("See you soon !")
        quit()
    elif(user_in.__eq__("1")):
        print("Temporary menu placeholder")
        quit()
        #Find a way to execute the general_menu file...
    elif(user_in.__eq__("2")):
        number_of_menus = meal_arg_input() #Also considers "back" and "exit"
        origin_sequence = user.get_last_user_meal()
        print("Generating " + str(number_of_menus) + " menu(s)...\n")
        for i in range(number_of_menus):
            true_origin_sequence = deepcopy(origin_sequence)
            generated_sequence = generator.generate_meal(origin_sequence.get_ingredients())
            generator.explain_meal(true_origin_sequence.get_ingredients(), generated_sequence.get_ingredients())
            origin_sequence = generated_sequence
            user.store_user_meal(generated_sequence)
        print("Done ! Here you go ;)\n")
        quit()
    else:
        print("Unrecognized input, please try again")
        back_input_after_2(user, generator);
        quit()