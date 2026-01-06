from itertools import combinations
def solution(numbers):
    answer=list(combinations(numbers,2))
    num_lst=[]
    for i in answer:
        num_lst.append(sum(i))
        
        
    return sorted(list(set(num_lst)))