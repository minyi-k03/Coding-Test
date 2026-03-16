import sys
input = sys.stdin.readline

x,y = map(int,input().split())

z = (y*100)//x

#Exception Case
if z >= 99:
    print(-1)
    sys.exit()

left = 1
right = 1000000000
ans = 0

#Main Logic
while left<=right:
    mid = (left+right)//2
    
    new_z = ((y+mid)*100)//(x+mid)
    
    if new_z > z:
        ans = mid
        right = mid - 1
        
    else:
        left = mid + 1
        
        
print(ans)
        