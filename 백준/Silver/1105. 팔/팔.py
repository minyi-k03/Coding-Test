import sys
input = sys.stdin.readline
L,R = map(int,input().split())
str_L = str(L)
str_R = str(R)

if len(str_L) != len(str_R):
    print(0)
    
else:
    count = 0
    for i in range(len(str_L)):
        if str_L[i] == '8' and str_R[i] == '8':
            count += 1
            
        elif str_L[i] != str_R[i]:
            break
            
            
    print(count)
    
    