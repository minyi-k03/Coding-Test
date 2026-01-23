import sys
input = sys.stdin.readline

N = int(input())
info = []

for _ in range(N):
    age,name = map(str,input().split())
    info.append([int(age),name])
    
info.sort(key = lambda x:x[0])

for i in range(N):
    print(info[i][0],info[i][1])