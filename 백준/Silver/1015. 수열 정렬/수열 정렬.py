import sys
input = sys.stdin.readline

N = int(input()) #전체 배열 크기 입력
nums = list(map(int,input().split())) #숫자들 입력
p = [0]*N

for i in range(N):
    for j in range(N):
        #같은 데이터에 대한 비교 방지
        if nums[j] < nums[i]:
            p[i] += 1
            
        elif nums[i] == nums[j] and j<i:
            p[i] += 1
            
print(*p)
            