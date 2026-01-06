from collections import deque
def bfs(data,start,end):
    rows = len(data)
    cols = len(data[0])
    Queue = deque([(start,start)]) #(노드,경로)
    visited = {start}
    length = 1
    
    while Queue:
        (row,col),path = Queue.popleft()
        
        if (row,col) == end:
            return len(path)//2
        
        
        for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
            dx,dy = row+x,col+y
            if 0<=dx<rows and 0<=dy<cols and data[dx][dy] == 1 and (dx,dy) not in visited:
                Queue.append(((dx,dy),path+(dx,dy)))
                visited.add((dx,dy))
                length += 1
            
            
        
    return -1
            
        
            
    
        
def solution(maps):
    
    start = (0,0)
    end = (len(maps)-1,len(maps[0])-1)
    
    path = bfs(maps,start,end)
    
    
    
    
    
    return path