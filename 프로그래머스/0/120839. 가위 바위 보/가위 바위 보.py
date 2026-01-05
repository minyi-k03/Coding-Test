def solution(rsp):
    answer = ''
    rock,scissors,paper="0","2","5"
    
    for i in rsp:
        if i=="2":
            answer+=rock
        elif i=="0":
            answer+=paper
        elif i=="5":
            answer+=scissors
    
    
    
    return answer