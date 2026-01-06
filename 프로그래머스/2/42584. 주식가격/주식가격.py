def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i,price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        
        stack.append(i)
    
    while stack:
        i = stack.pop()
        answer[i] = len(prices)-i-1
    
    return answer