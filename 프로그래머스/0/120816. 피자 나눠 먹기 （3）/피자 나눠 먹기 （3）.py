def solution(slice, n):
    answer=n//slice
    
    if answer*slice<n:
        answer+=1
    
    return answer