def solution(food):
    answer = ''
    tmp=''
    for idx,val in enumerate(food[1:]):
        for j in range(int(val//2)):
            tmp+=str(idx+1)
            
    answer+=tmp+"0"+tmp[::-1]
    
    
    return answer