import sys
input = sys.stdin.readline

#N과 L입력
N,L = map(int,input().split())


for i in range(L,101):
    temp = (i*(i-1))//2
    numerator = N-temp
    
    if numerator%i == 0:
        x = numerator//i
        
        if x>=0:
            for j in range(i):
                print(x+j,end=' ')
                
            sys.exit()
            
            
            
print(-1)
             
            
    
        

        