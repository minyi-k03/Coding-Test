import sys
input = sys.stdin.readline
N = int(input())
loc = []

#Input Location
for _ in range(N):
    x,y = map(int,input().split())
    loc.append([x,y])
    
loc.sort(key = lambda x:(x[0],x[1]))
 
for i in range(N):
    print(loc[i][0], loc[i][1])