#Dynamic Programming (동적 계획법을 이용한 풀이법), #재귀적 호출 #피보나치 수열
def solution(n):
    dp = [0 for i in range(n)] #전체 배열 설정
    dp[0], dp[1] = 1,2 #미리 배열에 저장함으로써 재귀호출시 중복 연산을 줄인다
    
    for i in range(2,n):
        dp[i] = (dp[i-1] + dp[i-2])%1000000007
        
    
    
    return dp[n-1]