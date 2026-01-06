def solution(land):
    rows = len(land)
    cols = len(land[0])

    dp = [[0] * cols for _ in range(rows)]  # DP 테이블 초기화

    for j in range(cols):
        dp[0][j] = land[0][j]  # 첫 번째 행 값 초기화

    for i in range(1, rows):
        for j in range(cols):
            max_val = 0
            for k in range(cols):
                if k != j:  # 같은 열은 제외
                    max_val = max(max_val, dp[i - 1][k])
            dp[i][j] = land[i][j] + max_val  # 현재 칸의 최대 점수 계산

    return max(dp[rows - 1])  # 마지막 행에서 최대 값 반환