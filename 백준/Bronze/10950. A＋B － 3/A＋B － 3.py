import sys
input = sys.stdin.readline

epoch = int(input())

for _ in range(epoch):
    a,b = map(int,input().split())
    print(a+b)