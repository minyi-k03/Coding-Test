import sys
input = sys.stdin.readline

T = int(input())
lst = []

#13개의 단어 입력
for _ in range(T):
    lst.append(input().strip())
    
#중복 제거
lst = list(set(lst))

#정렬
lst.sort(key = lambda x:(len(x),x))

#출력
for i in lst:
    print(i)
