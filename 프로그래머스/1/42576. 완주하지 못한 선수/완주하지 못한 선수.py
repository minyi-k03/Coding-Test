#Collections에 있는 Counter함수를 이용하여 푸는 문제 효율성은 비슷함
from collections import Counter
def solution(participant, completion):
    answer = ''
    
    dict_result=Counter(participant)-Counter(completion)
    
    return list(dict_result.keys())[0]