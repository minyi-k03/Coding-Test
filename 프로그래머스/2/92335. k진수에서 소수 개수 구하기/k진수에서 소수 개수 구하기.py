import math
def solution(n, k):
    answer = 0
    tmp = ""
    while n>0:
        tmp += str(n%k)
        n = n//k
        
    
    tmp = list(filter(None,tmp[::-1].split("0")))
    
    for i in tmp:
        if int(i) == 1:
            continue
            
        elif int(i) == 2 or int(i) == 3:
            answer += 1
        else:
            answer += 1
            for j in range(2,int(math.sqrt(int(i)))+1):
                if int(i)%j == 0:
                    answer -= 1
                    break
                    
        
            
    
    
    
    
    
    
    
    return answer