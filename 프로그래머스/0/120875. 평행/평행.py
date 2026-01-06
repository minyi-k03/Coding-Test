from itertools import combinations
#Git Hub에서 참고함

def get_inclination(dot0, dot1):
    return abs(dot0[1] - dot1[1]) / abs(dot0[0] - dot1[0])


def solution(dots):
    for a, b in combinations(combinations(dots, 2), 2):
        if set(tuple(_) for _ in a).isdisjoint(set(tuple(_) for _ in b)):
            # ((a, b), (c, d)) OR ((a, c), (b, d)) OR ((a, d),(b, c))
            if get_inclination(*a) == get_inclination(*b):
                return 1
    return 0