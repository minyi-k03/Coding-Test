import math
from itertools import combinations
def is_prime_number(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True
def solution(nums):
    answer = -1
    count=0
    result=list(combinations(nums,3))
    
    for i in result:
        if is_prime_number(sum(i)):
            count+=1
        
    return count

    