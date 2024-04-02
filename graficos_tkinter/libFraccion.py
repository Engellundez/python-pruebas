class Fraccion():
    def __init__(self, num=0, den=1):
        if isinstance(num, int):
            self.num = num
        else:
            self.num = 0
        
        if isinstance(den, int) and den != 0:
            self.den = den
        else:
            self.den = 1
        
        self.simplificada()
    
    def __str__(self):
        return f"({self.num}/{self.den})"
    
    def __mul__(self, obj):
        n = self.num * obj.num
        d = self.den * obj.den
        x = Fraccion(n,d)
        x.simplifica()
        return x
    
    def __div__(self, obj):
        n = self.num * obj.den
        d = self.den * obj.num
        x = Fraccion(n,d)
        x.simplificada()
        return x
    
    def __add__(self, obj):
        n = self.num * obj.den + self.den * obj.num
        d = self.den * obj.den
        x = Fraccion(n,d)
        x.simplificada()
        return x
    
    def __sub__(self, obj):
        n = self.num * obj.den + self.den * obj.num
        d = self.den * obj.den
        x = Fraccion(n,d)
        x.simplificada()
        return x