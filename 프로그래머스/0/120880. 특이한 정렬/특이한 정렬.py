def solution(numlist, n):
    answer = []
    distance=[]
    
    for i in numlist:
        distance.append([abs(i-n),i])
    distance.sort()
    
    
    
    for i in range(len(distance)-1):
        if distance[i][0]==distance[i+1][0] and distance[i][1]<distance[i+1][1]:
            distance[i][1],distance[i+1][1]=distance[i+1][1],distance[i][1]
        
        answer.append(distance[i][1])
         
    answer.append(distance[-1][1])
    
    return answer