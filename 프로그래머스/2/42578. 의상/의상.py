def solution(clothes):
    clothes_dict = {}
    answer = 1
    
    for i in clothes:
        if i[1] not in clothes_dict:
            clothes_dict[i[1]] = 1
        else:
            clothes_dict[i[1]] += 1
    
    
    for key in clothes_dict:
        answer*=(clothes_dict[key]+1)
        
    
    return answer-1