def solution(intStrs, k, s, l):
    answer = []
    ret=[]
    for i in range(len(intStrs)):
        answer.append(intStrs[i][s:s+l])
    
        if(int(answer[i])>k):
            ret.append(int(answer[i]))
            
    
    
    return ret