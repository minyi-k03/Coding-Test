import sys
input = sys.stdin.readline
single = [] #기타줄 낱개가격
package = [] #패키지 가격

#끊어진 기타줄, 기타줄 브랜드 개수 입력
N,M = map(int,input().split())


#Input
for _ in range(M):
    a,b = map(int,input().split()) #6개 패키지 가격, 낱개가격 입력
    package.append(a)
    single.append(b)

#Package,Single 배열 오름차순 정렬
package.sort()
single.sort()

#가장 최저가 설정
min_package = package[0]
min_single = single[0]

#패키지 가격이 낱개 * 6개보다 비싼경우
if min_package > min_single*6:
    min_package = min_single*6

#패키지 가격 + 낱개 가격
result = (N//6)*min_package + min((N%6)*min_single,min_package)
        
print(result)