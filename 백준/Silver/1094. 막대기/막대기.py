import math 
import sys
input = sys.stdin.readline
stick = 64
lst = []
x = int(input())
total = 0


while True:
    
    if stick <= x:
        if total+stick <= x:
            total += stick
            lst.append(stick)
        
    
    if total == x:
        print(len(lst))
        break
    
    stick = stick//2