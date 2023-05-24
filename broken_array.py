from typing import List, Tuple, Union


def read_input() -> Tuple[List[str], str]:
    _ = input()
    target = input()
    nums = input().split()
    return nums, target


def broken_search(nums: List[str], target: str) -> Union[str, int]:
    start: int = 0
    end: int = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[start] <= nums[mid]:
            if nums[start] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[mid] < target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1


def main():
    return


if __name__ == '__main__':
    main()
