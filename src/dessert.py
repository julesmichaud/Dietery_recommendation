'''
Created on Jun 20, 2022

@author: valerio
'''

from src.service import Service

class Dessert(Service):
    '''
    classdocs
    '''


    def __init__(self, ingredients, time, quantity,):
        '''
        Constructor
        '''
        super.__init__(self, ingredients, time, quantity)
        