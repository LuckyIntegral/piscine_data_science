from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    '''Class for the King family'''
    def __init__(self, first_name, is_alive=True):
        '''Constructor for the King class'''
        Baratheon.__init__(self, first_name, is_alive)

    def set_eyes(self, eyes):
        '''Method to set the eyes of the character'''
        self.eyes = eyes

    def get_eyes(self):
        '''Method to return the eyes of the character'''
        return self.eyes

    def set_hairs(self, hairs):
        '''Method to set the hairs of the character'''
        self.hairs = hairs

    def get_hairs(self):
        '''Method to return the hairs of the character'''
        return self.hairs
