def solution(score):
    answer = []
    avg=[]
    
    for i in score:
        avg.append(sum(i)/len(i))
        
    sort_arr=sorted(avg,reverse=True)
    
    for i in avg:
        answer.append(sort_arr.index(i)+1)
    
    
    
    return answer