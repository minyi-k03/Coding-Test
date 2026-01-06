def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    print(citations)
    
    for idx,val in enumerate(citations):
        if idx+1 <= val:
            answer+=1
            
            
    return answer
    
    