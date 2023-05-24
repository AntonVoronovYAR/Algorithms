def read_input():
    """Считывание входящих данных."""
    matrix = []
    n = int(input()) * 2
    for _ in range(4):
        matrix += [i for i in input()]
    return matrix, n


def solution(matrix, n):
    """Алгоритм подсчета очков."""
    result = 0
    clean = list(set(matrix))
    for i in clean:
        if i.isdigit() and matrix.count(i) <= n:
            result += 1
    return result


print(solution(*read_input()))
