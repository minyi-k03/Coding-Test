import sys
input = sys.stdin.readline

s = int(input()) #전체 배열 길이
l = list(map(int,input().split())) #배열 개수
n = int(input())

#배열 L에 N이 있는지에 대한 여부 판단
if n in l:
    print(0)
    sys.exit()

l.append(n)
l.sort()
idx = l.index(n) #N에 대한 인덱스 위치

if idx == 0:
    left_bound = 0
else:
    left_bound = l[idx-1]
right_bound = l[idx+1]

total = (n-left_bound)*(right_bound-n)-1

print(total)

 