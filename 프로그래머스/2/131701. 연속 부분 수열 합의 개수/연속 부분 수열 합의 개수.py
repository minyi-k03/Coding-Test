def solution(elements):
    sums = set()
    n = len(elements)
    extended_elements = elements + elements  # 원형 수열 처리를 위한 배열 확장

    for length in range(1, n + 1):  # 부분 수열 길이
        for start in range(n):  # 시작 위치
            current_sum = sum(extended_elements[start:start + length])
            sums.add(current_sum)

    return len(sums)