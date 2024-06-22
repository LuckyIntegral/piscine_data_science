from abc import ABC, abstractmethod


class Character(ABC):
    '''Abstract class for a character'''
    def __init__(self, first_name, is_alive=True):
        '''Constructor for the Character class'''
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        ''' Abstract method to kill the character '''
        pass


class Stark(Character):
    '''Class for the Stark family'''
    def __init__(self, first_name, is_alive=True):
        '''Constructor for the Stark class'''
        super().__init__(first_name, is_alive)

    def die(self):
        '''Method to kill the character'''
        self.is_alive = False
