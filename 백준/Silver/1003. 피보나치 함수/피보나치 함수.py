import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


memo = [None]*41
memo[0] = [1,0]
memo[1] = [0,1]

#Function Fibonacci
def recursive(N):
    if memo[N] is not None:
        return memo[N]
    
    count_n_1 = recursive(N-1)
    count_n_2 = recursive(N-2)
    
    current_result = [count_n_1[0]+count_n_2[0], + count_n_1[1] + count_n_2[1]]
    
    memo[N] = current_result
    
    return current_result


#Input Test Case
T = int(input())

for _ in range(T):
    N = int(input())
    result = recursive(N)
    print(result[0],result[1])
    