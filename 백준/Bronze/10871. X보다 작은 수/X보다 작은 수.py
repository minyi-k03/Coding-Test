import sys
input = sys.stdin.readline
N,X = map(int,input().split())
lst = []

num = list(map(int,input().split()))
    
for i in num:
    if i<X:
        lst.append(i)
        
print(*lst)
    