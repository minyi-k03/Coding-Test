import sys
input = sys.stdin.readline

epoch = int(input())
lst = []

for i in range(epoch):
    a,b = map(int,input().split())
    lst.append(a+b)
    
for i in range(epoch):
    print("Case #"+str(i+1)+": "+str(lst[i]))
