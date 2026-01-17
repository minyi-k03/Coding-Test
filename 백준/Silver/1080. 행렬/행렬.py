import sys
input = sys.stdin.readline
N,M = map(int,input().split())
A = []
B = []

#Input A
for _ in range(N):
    a = list(map(int,input().rstrip()))
    A.append(a)
    
#Input B
for _ in range(N):
    b = list(map(int,input().rstrip()))
    B.append(b)
    

#3x3 Flip
def flip(row,col):
    for i in range(row,row+3):
        for j in range(col,col+3):
            A[i][j] = 1-A[i][j]
            
count = 0
#Matrix Recursion and flip
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            flip(i,j)
            count+=1
            
#Matrix A and B Value Compare
for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            print(-1)
            sys.exit()
print(count)