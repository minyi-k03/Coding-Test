import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N,Jimin,Hansu = map(int,input().split())

#Divide and Conquer
def DNC(i,j,h): #Parameter i 는 라운드 수 조정
    if(j+1)//2 == (h+1)//2:
        return i
        
    return DNC(i+1,(j+1)//2,(h+1)//2)
    
result = DNC(1,Jimin,Hansu)  

print(result)