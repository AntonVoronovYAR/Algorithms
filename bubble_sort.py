from copy import deepcopy


def read_input():
    n = int(input())
    numbers = [int(i) for i in input().split()]
    return n, numbers


def bubble_sort(n, numbers):
    first_list = deepcopy(numbers)
    while n > 1:
        flag = False
        for i in range(1, n):
            if numbers[i - 1] > numbers[i]:
                numbers[i - 1], numbers[i] = numbers[i], numbers[i - 1]
                flag = True
        if flag:
            print(*numbers)
        n -= 1
    if numbers == first_list:
        print(*numbers)


n, numbers = read_input()
bubble_sort(n, numbers)
