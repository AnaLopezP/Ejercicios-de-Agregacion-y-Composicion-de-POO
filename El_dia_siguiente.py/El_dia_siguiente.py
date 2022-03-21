class CIUDAD:
    def __init__(self, NY, LA):
        self.NY = NY
        self.LA = LA

class EDIFICIO(CIUDAD):
    def __init__(self, NY, LA, A, B, C):
        super().__init__(NY, LA)
        self.A = A
        self.B = B
        self.C = C