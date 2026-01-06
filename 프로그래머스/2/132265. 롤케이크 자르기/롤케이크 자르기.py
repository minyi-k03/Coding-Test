def solution(topping):
    answer = 0
    p1 = topping #철수
    p1_hash = {} #철수 해시 요소 판별
    p2_hash = {} #철수 동생 해시 요소 판별
    
    for i in topping: #철수가 토핑을 전부 가지고 있는 상황
        if i not in p1_hash.keys():
            p1_hash[i] = 1
        elif i in p1_hash.keys():
            p1_hash[i] += 1
    
    
    
    
    while len(p2_hash.keys())<=len(p1_hash.keys()):
        
        popping = p1.pop() #p1에서 요소 하나를 pop함
        p1_hash[popping] -= 1 #p1_hash의 value 값을 줄임
        
        if popping not in p2_hash.keys(): #pop한 키 값이 p2_hash의 키값에 없다면
            p2_hash[popping] = 1 #p2_hash 딕셔너리에 key,value 추가
            
        elif popping in p2_hash.keys(): #pop한 키 값이 p2_hash의 키 값에 있다면
            p2_hash[popping] += 1
            
            
        if p1_hash[popping] == 0: #key = popping의 value 값이 0인 경우    
            p1_hash.pop(popping,None)
            
        if len(p1_hash.keys()) == len(p2_hash.keys()):
            answer += 1
            
            
        
        
        
        
        
    
    
    
    
    
    return answer