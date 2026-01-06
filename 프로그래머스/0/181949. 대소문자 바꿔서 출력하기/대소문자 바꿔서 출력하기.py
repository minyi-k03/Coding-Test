str = input()
answer=[]
for i in str:
    if 'a'<=i<='z':
        answer.append(i.upper())
    elif 'A'<=i<='Z':
        answer.append(i.lower())
        
print("".join(answer))
