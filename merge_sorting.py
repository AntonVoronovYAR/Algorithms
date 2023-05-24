from typing import List


def merge(arr: list, lf: int, mid: int, rg: int) -> List:
    result = []
    left = arr[lf:mid]
    right = arr[mid:rg]
    i_left = i_right = 0
    while len(result) < len(left) + len(right):
        if left[i_left] <= right[i_right]:
            result.append(left[i_left])
            i_left += 1
        else:
            result.append(right[i_right])
            i_right += 1
        if i_right == len(right):
            result += left[i_left:]
            break
        if i_left == len(left):
            result += right[i_right:]
            break
    return result


def merge_sort(arr: list, lf: int, rg: int) -> None:
    if rg - lf >= 2:
        mid = (lf + rg) // 2
        merge_sort(arr, lf, mid)
        merge_sort(arr, mid, rg)
        arr[lf:rg] = merge(arr, lf, mid, rg)
