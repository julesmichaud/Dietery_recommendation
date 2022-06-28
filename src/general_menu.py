'''
Created on 22 juin 2022

@author: Aurelien Giroux
'''

def is_back(user_in):
    str.lower(user_in)
    if(user_in.__eq__("back")):
        return True
    return False

def is_exit(user_in):
    str.lower(user_in)
    if(user_in.__eq__("exit")):
        return True
    return False

if __name__ == '__general_menu__':
    pass