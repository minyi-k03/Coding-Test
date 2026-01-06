import math
def solution(n):
    answer = 0
    num=math.sqrt(n)
    
    if float(num).is_integer():
        return pow(num+1,2)
    elif float(num).is_integer()==False:
        return -1
    
    
    