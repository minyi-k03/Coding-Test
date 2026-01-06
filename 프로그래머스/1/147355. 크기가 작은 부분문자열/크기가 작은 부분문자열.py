def solution(t, p):
    answer = 0
    tmp=[]
    for i in range(len(t)):
        if i+len(p)-1!=len(t):
            tmp.append(t[i:i+len(p)])
        else:
            break
    
    for i in tmp:
        if int(i)<=int(p):
            answer+=1
    
    
    
    return answer