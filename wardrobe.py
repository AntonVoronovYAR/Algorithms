from typing import List


def read_input() -> List[str]:
    _ = int(input())
    color_nums = input().split()
    return color_nums


def solution(color_nums: List[str], n=3) -> None:
    counted_values = [0] * n
    for i in color_nums:
        counted_values[int(i)] += 1

    result = []
    for color, count in enumerate(counted_values):
        result.extend([color] * count)
    print(*result)


color_nums = read_input()
solution(color_nums)
