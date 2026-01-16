import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [0,0,1,-1] #x좌표 이동
dy = [1,-1,0,0] #y좌표 이동


def DFS(row,col):
      
    for i in range(4):
        nx = row+dx[i] #탐색할 row
        ny = col+dy[i] #탐색할 col
        
        # 1. 범위 체크 (가장 먼저!)
        if 0 <= nx < N and 0 <= ny < M:
            # 2. 배추가 있으면(1) -> 방문 처리(0) 하고 -> 더 깊이 들어감(재귀)
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0 # 방문 했다고 표시 (배추 뽑기)
                DFS(nx, ny)       # 거기서 또 탐색 시작
        
    return worm

T = int(input()) #Input Test Case 입력

while T > 0:
    M,N,K = map(int,input().split())#M = 가로(col), N = 세로(row), K = 배추 개수
    graph = [[0 for _ in range(M)]for _ in range(N)] #Map Graph Initializing
    worm = 0
    #배추 심기
    for _ in range(K):
        col,row = map(int,input().split())
        graph[row][col] = 1
        
        
    #Map Graph DFS Execution
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                DFS(i,j)
                worm+=1
                
    print(worm)
    T-=1
            