





from math import *

def sum_bigInteger(a, b):
    
    
    res = str((int(a[-1]) + int(b[-1])) % 10 )
    res1 = (int(a[-1]) + int(b[-1])) // 10
    for i in range(-2, -(min(len(a), len(b))) - 1, -1):
            temp1 = (int(a[i]) + int(b[i]))
            if res1 == 1:
                res = str(temp1 + 1 % 10) + res
                res1 = ((temp1 + 1) // 10)
            else:
                res =  str(temp1 % 10) + res
                res1 = (temp1 // 10)
            
    for i in range(0, abs(len(a) - len(b))):
         if res1 == 1:
              

if __name__ == '__main__':
    for t in range(int(input())):
        p, q = map(int,  input().split())
        s = input()
        s2 = input()
        maxs = s.replace('5', '6')
        mins = s.replace('6', '5')
        maxs2 = s2.replace('5', '6')
        mins2 = s2.replace('6', '5')

        
        