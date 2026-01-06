def solution(dirs):
    answer = 0
    x,y = 0,0
    visited = []
    
    for i in dirs:
        dx,dy = x,y #x,y 좌표 갱신
        
        if i == "U":
            dy = min(y+1,5)
        
        if i == "D":
            dy = max(y-1,-5)
            
        if i == "R":
            dx = min(x+1,5)
            
        if i == "L":
            dx = max(x-1,-5)
        
        
        if (dx,dy) == (x,y):
            continue
            
        path = str(x)+str(y)+str(dx)+str(dy)
        reverse = str(dx)+str(dy)+str(x)+str(y)
        
        if path not in visited and reverse not in visited:
            visited.append(path)
            answer += 1
        
            
        x,y = dx,dy
        
    
    
    return answer