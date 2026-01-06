def solution(msg):
    answer = [0]
    dic = {}
    for i in range(1,27):
        dic[chr(64+i)] = i
        
    tmp = ''
    dic_len = len(dic) #딕셔너리 길이
    
    for i in msg:
        tmp += i
        
        if tmp in dic:
            answer[-1] = dic[tmp]
        
        elif tmp not in dic:
            dic_len += 1
            dic[tmp] = dic_len #새로운 문자 딕셔너리에 추가
            tmp = i 
            answer.append(dic[tmp])
            
            
        
     
    return answer