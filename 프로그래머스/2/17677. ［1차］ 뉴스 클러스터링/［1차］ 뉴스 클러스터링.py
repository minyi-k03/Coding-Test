from collections import Counter
def solution(str1, str2):
    answer = 0
    str1_search = []
    str2_search = []
    
    for i in range(len(str1)-1):
        tmp = str1[i:i+2]
        if tmp.isalpha():
            str1_search.append(tmp.upper())
        
        
    
    for i in range(len(str2)-1):
        tmp = str2[i:i+2]
        if tmp.isalpha():
            str2_search.append(tmp.upper())
        
    
    str1_search = Counter(str1_search)
    str2_search = Counter(str2_search)
    
    
    intersection_search = list((str1_search & str2_search).elements())
    union_search = list((str1_search | str2_search).elements())
    
    if len(intersection_search) == 0 and len(union_search) == 0:
        return 65536
    else:
        return int(len(intersection_search)/len(union_search)*65536)