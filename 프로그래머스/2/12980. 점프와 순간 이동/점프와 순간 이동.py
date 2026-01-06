def solution(n): #순간이동=현재까지 온 거리x2 점프=K칸 앞으로 점프 가능 대신 K만큼 배터리 사용
    ans = 0
    battery=0
    current_distance=0
    
    
    while n:
        if n%2==0:
            n/=2
        else:
            n-=1
            battery+=1
        
    
    return battery