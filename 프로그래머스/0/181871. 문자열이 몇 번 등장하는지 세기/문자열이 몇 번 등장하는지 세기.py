def solution(myString, pat):
    answer = 0
    idx=0
    idx2=len(pat)
    while idx2<=len(myString):
        if myString[idx:idx2]==pat:
            answer+=1
            
        idx+=1
        idx2+=1
    
        
    
    
    return answer