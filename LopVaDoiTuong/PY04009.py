
from math import *
def chuyen_complex(result):
    
    tp1 = result.real
    tp2 = str(result.imag)
    mul = ''
    if(tp2[0] == '-'):
        mul = '-'
    else:
        mul = '+'
    print('{} {} {}i'.format(int(tp1), mul ,int(abs(result.imag))), end="")



if __name__ == '__main__':
    for t in range(int(input())):
        x1, y1, x2, y2 = map(int, input().split())
        z1 = complex(x1, y1)
        z2 = complex(x2, y2)
        result1 = (z1 + z2) * z1
        result2 = (z1 + z2) ** 2
        chuyen_complex(result1)
        print(", ", end="")
        chuyen_complex(result2)
        print()