import sys
input = sys.stdin.readline

word = input()
temp = ''

for i in word:
    if 'a'<= i <= 'z':
        temp += i.upper()
        
    else:
        temp += i.lower()
        
print(temp)