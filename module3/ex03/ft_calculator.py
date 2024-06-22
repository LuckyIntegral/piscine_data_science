
class calculator:
    '''aplly an operation to a list of numbers'''
    def __init__(self, lst):
        '''Constructor for the calculator class'''
        self.lst = lst

    def __add__(self, nbr):
        '''Method to add a number to the list'''
        self.lst = [i + nbr for i in self.lst]
        print(self.lst)

    def __mul__(self, nbr):
        '''Method to substract a number to the list'''
        self.lst = [i * nbr for i in self.lst]
        print(self.lst)

    def __sub__(self, nbr):
        '''Method to multiply a number to the list'''
        self.lst = [i - nbr for i in self.lst]
        print(self.lst)

    def __truediv__(self, nbr):
        '''Method to divide a number to the list'''
        if nbr != 0:
            self.lst = [i / nbr for i in self.lst]
        print(self.lst)
