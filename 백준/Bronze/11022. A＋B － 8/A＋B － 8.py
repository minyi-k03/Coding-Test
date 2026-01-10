import sys
input = sys.stdin.readline
lst = []

epoch = int(input())

for _ in range(epoch):
    a,b = map(int,input().split())
    lst.append([a,b,a+b]) #입력 값 a,b,a+b 저장
    
for i in range(0,epoch):
    print("Case #"+str(i+1)+": "+str(lst[i][0])+" + "+str(lst[i][1])+" = "+str(lst[i][2]))