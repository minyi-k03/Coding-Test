import sys
input = sys.stdin.readline


T = int(input())

while T > 0:
    #좌표 입력
    x1,y1,x2,y2 = map(int,input().split())
    stars = int(input())
    
    count = 0
    
    for _ in range(stars):
        cx,cy,r = map(int,input().split())
        
        #출발지점과 행성 사이의 거리
        d1 = (x1-cx)**2 + (y1-cy)**2
        
        #도착지점과 행성 사이의 거리
        d2 = (x2-cx)**2 + (y2-cy)**2
        
        r2 = r**2
        
        if(d1 < r2 and d2 > r2 ) or (d2 < r2 and d1 > r2):
            count += 1
            
    print(count)
    T -= 1