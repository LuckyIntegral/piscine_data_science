class calculator:
    '''calculator class for lists'''
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        print(f'Dot product is: {sum([a * b * 1.0 for a, b in zip(V1, V2)])}')

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        print(f'Add Vector is : {[a + b * 1.0 for a, b in zip(V1, V2)]}')

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        print(f'Sous Vector is: {[a - b * 1.0 for a, b in zip(V1, V2)]}')
