def solution(s):
    answer = []
    lst = []
    
    for i in s.split("},"):
        lst.append(i.replace("{","").replace("}","").split(","))
    
    lst.sort(key=len)
    
    for i in lst:
        for j in i:
            if len(answer) == 0:
                answer.append(int(j))
                
            if int(j) not in answer:
                answer.append(int(j))
    
    
    return answer