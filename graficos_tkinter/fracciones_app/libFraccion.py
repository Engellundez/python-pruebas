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

        self.simplifica()

    def __str__(self):
        if self.num == 0 and self.den == 1:
            return ''
        
        return f"({self.num}/{self.den})"

    def __mul__(self, obj):
        n = self.num * obj.num
        d = self.den * obj.den
        x = Fraccion(n, d)
        x.simplifica()
        return x

    def __truediv__(self, obj):
        n = self.num * obj.den
        d = self.den * obj.num
        x = Fraccion(n, d)
        x.simplifica()
        return x

    def __add__(self, obj):
        n = self.num * obj.den + self.den * obj.num
        d = self.den * obj.den
        x = Fraccion(n, d)
        x.simplifica()
        return x

    def __sub__(self, obj):
        n = self.num * obj.den - self.den * obj.num
        d = self.den * obj.den
        x = Fraccion(n, d)
        x.simplifica()
        return x

    def __eq__(self, obj):
        return (self.num/self.den == obj.num/obj.den)

    def simplifica(self):
        def mcd(a, b):
            if b == 0:
                return a

            return mcd(b, a % b)

        d = mcd(self.num, self.den)
        self.num = int(self.num/d)
        self.den = int(self.den/d)
