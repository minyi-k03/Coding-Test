def solution(babbling):
    answer = 0
    line = ["aya", "ye", "woo", "ma"]
    for i in range(len(babbling)):
        b = str(babbling[i])
        for j in range(len(b)):
            if "aya" in b[0:3]:
                b = b.replace(b[0:3], "")
            elif "ye" in b[0:2]:
                b = b.replace(b[0:2], "")
            elif "woo" in b[0:3]:
                b = b.replace(b[0:3], "")
            elif "ma" in b[0:2]:
                b = b.replace(b[0:2], "")
            elif len(b) == 0:
                answer += 1
                break
            else:
                break
    return answer
