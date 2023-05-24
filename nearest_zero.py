def read_input():
    """Считывание входящих данных."""
    n = int(input())
    street = [int(i) for i in input().split()]
    return street, n


def solution(street, n):
    """Алгоритм подсчета расстояний."""
    ranges = [0 for _ in range(n)]
    index_zero = []

    for index, num in enumerate(street, start=1):
        if num == 0:
            index_zero.append(index)

    ranges[:index_zero[0]] = list(range(0, index_zero[0]))[::-1]
    ranges[index_zero[-1]:] = list(range(1, n - index_zero[-1] + 1))

    for i in range(len(index_zero) - 1):
        r = index_zero[i + 1] - index_zero[i]
        if r != 1:
            r1 = r // 2
            r2 = r - r1 - 1
            ranges[index_zero[i]:index_zero[i] + r1] = list(
                range(1, r1 + 1)
            )
            ranges[index_zero[i] + r1:index_zero[i] + r1 + r2] = list(
                range(1, r2 + 1)
            )[::-1]
    return ranges


print(*solution(*read_input()))
