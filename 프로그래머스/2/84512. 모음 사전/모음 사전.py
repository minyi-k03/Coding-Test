from itertools import product 
def solution(word):
    answer = 0
    data = ['A','E','I','O','U']
    lst_product = []
    
    for i in range(1,len(data)+1):
        for j in product(data, repeat=i):
            lst_product.append(j)
            
    lst_product.sort()
    
    for i in lst_product:
        answer += 1
        if "".join(i) == word:
            return answer
        
    
    return answer