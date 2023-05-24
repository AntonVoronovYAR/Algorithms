def read_input():
    _ = int(input())
    numbers = [i for i in input().split()]
    return numbers


def comparor(a, b):
    ab = int(a + b)
    ba = int(b + a)
    if ab <= ba:
        return True
    elif ba > ab:
        return False


def big_number_sort_by_comparator(array, func):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and func(array[j-1], item_to_insert):
            array[j] = array[j-1]
            j -= 1
        array[j] = item_to_insert


numbers = read_input()
big_number_sort_by_comparator(numbers, comparor)
print(''.join(numbers))
