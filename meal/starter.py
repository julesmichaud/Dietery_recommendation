'''
Created on Jun 20, 2022

@author: valerio
'''

from meal.service import Service

class Starter(Service):
    '''
    classdocs
    '''


    def __init__(self, ingredients, time, quantity,):
        '''
        Constructor
        '''
        super.__init__(self, ingredients, time, quantity)