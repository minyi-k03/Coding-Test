#itertools를 사용하여 시간복잡도를 줄였다
from itertools import combinations
def solution(number):
    result=list(combinations(number,3))
    answer=0
    
    for i in result:
        if sum(i)==0:
            answer+=1
    return answer