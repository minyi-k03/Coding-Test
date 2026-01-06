from itertools import permutations
def solution(k, dungeons):
    answer = 0
    count = 0
    tmp = k
    for i in permutations(dungeons,len(dungeons)):
        for essential,reduce in i:
            if tmp >= essential:
                tmp -= reduce
                count += 1
             
            else:
                tmp = k
                answer = max(answer,count)
                count = 0
                break
                
        
    
              
        
    
    
    
    
    return answer