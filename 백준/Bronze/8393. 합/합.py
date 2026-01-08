import sys
input = sys.stdin.readline

total = 0
a = int(input())

for i in range(1,a+1):
    total += i
    
print(total)