from typing import Tuple


def read_input() -> Tuple[str, str]:
    a = input()
    b = input()
    return a, b


def solution(a, b) -> bool:
    if len(a) > len(b):
        return False
    len_a = len(a)
    len_b = len(b)
    i, j = 0, 0
    while i < len_a and j < len_b:
        if a[i] == b[j]:
            i += 1
            j += 1
        else:
            j += 1

    if i == len(a):
        return True
    return False


a, b = read_input()
print(solution(a, b))
