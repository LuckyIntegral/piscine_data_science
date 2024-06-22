from S1E9 import Character


class Baratheon(Character):
    '''Class for the Baratheon family'''
    def __init__(self, first_name, is_alive=True):
        '''Constructor for the Baratheon class'''
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        '''Method to kill the character'''
        self.is_alive = False

    def __str__(self):
        '''Method to return the name of the character'''
        return f"Vector: ('{self.family_name}' '{self.eyes}' '{self.hairs}')"

    def __repr__(self):
        '''Method to return the name of the character'''
        return f"Vector: ('{self.family_name}' '{self.eyes}' '{self.hairs}')"


class Lannister(Character):
    '''Class for the Lannister family'''
    def __init__(self, first_name, is_alive=True):
        '''Constructor for the Lannister class'''
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        '''Method to kill the character'''
        self.is_alive = False

    @staticmethod
    def create_lannister(first_name, is_alive):
        '''Method to create a Lannister character'''
        return Lannister(first_name, is_alive)

    def __str__(self):
        '''Method to return the name of the character'''
        return f"Vector: ('{self.family_name}' '{self.eyes}' '{self.hairs}')"

    def __repr__(self):
        '''Method to return the name of the character'''
        return f"Vector: ('{self.family_name}' '{self.eyes}' '{self.hairs}')"
