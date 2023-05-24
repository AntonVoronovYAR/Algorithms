from random import randint
from typing import Union, List, Tuple


class Students:
    def __init__(self, name: str, tasks: int, penalty: int) -> None:
        self.name = name
        self.tasks = tasks
        self.penalty = penalty

    def __str__(self) -> str:
        return self.name

    def __lt__(self, other: Union[str, int]) -> bool:
        return ([-self.tasks, self.penalty, self.name] <
                [-other.tasks, other.penalty, other.name])


def quick_sort_in_place(results: List[Students], start: int, end: int) -> None:
    if start >= end:
        return
    i, j = start, end
    pivot = results[randint(start, end)]
    while i <= j:
        while results[i] < pivot:
            i += 1
        while results[j] > pivot:
            j -= 1
        if i <= j:
            results[i], results[j] = results[j], results[i]
            i += 1
            j -= 1
    quick_sort_in_place(results, start, j)
    quick_sort_in_place(results, i, end)


def read_input() -> Tuple[List, int]:
    results = []
    n = int(input())
    for i in range(n):
        name, tasks, penalty = input().split()
        results.append(Students(name, int(tasks), int(penalty)))
    return results, n


def main():
    results, n = read_input()
    quick_sort_in_place(results, 0, n-1)
    print(*results, sep='\n')


if __name__ == '__main__':
    main()
