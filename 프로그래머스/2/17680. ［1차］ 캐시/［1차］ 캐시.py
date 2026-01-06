from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque([])
    
    for i in range(len(cities)): #대소문자 구분 없이 이기 때문에 모두 대문자로 변환함
        cities[i] = cities[i].upper()
    
    for i in cities:
        if cacheSize == 0:
            return len(cities)*5
        
        elif len(cache) != cacheSize: #캐시가 다 안찬 경우
            if i in cache:
                cache.remove(i)
                cache.append(i)
                answer += 1
            else:
                cache.append(i)
                answer += 5
        elif len(cache) == cacheSize: #캐시가 다 찬경우
            if i not in cache: #cacheMiss
                cache.popleft()
                cache.append(i)
                answer += 5
            elif i in cache: #cacheHit
                cache.remove(i)
                cache.append(i)
                answer += 1
    
    return answer