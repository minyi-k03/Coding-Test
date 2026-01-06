def solution(arr):
    answer = []
    i=0
    while(i<len(arr)):
        
        if answer==[]:
            answer.append(arr[i])
            i+=1
        elif arr[i]==answer[-1]:
            del answer[-1]
            i+=1
        elif arr[i]!=answer[-1]:
            answer.append(arr[i])
            i+=1
    
    if answer==[]:
        answer.append(-1)
    
    return answer