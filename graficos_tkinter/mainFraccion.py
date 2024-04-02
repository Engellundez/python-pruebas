from .libFraccion import Fraccion
from .libFracMix import FracMix

def main():
    a = FracMix(2,3,4)
    b = a.toFraccion()
    
    print(a)
    print(b)
    
if __name__ == '__main__':
    main()