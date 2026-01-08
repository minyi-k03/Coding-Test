import sys
input = sys.stdin.readline
king = 1
queen = 1
rook = 2
bishop = 2
knight = 2
pawn = 8

K,Q,R,B,KN,P = map(int,input().split())

lst = []
lst.append(king-K)
lst.append(queen-Q)
lst.append(rook-R)
lst.append(bishop-B)
lst.append(knight-KN)
lst.append(pawn-P)

print(*lst)