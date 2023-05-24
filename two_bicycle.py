def read_input():
    right = int(input())
    money = [int(i) for i in input().split()]
    cost = int(input())
    return cost, money, right


def can_i_buy(cost, money, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if money[mid] >= cost > money[mid - 1] or mid == 0:
        return mid + 1
    elif money[mid] >= cost:
        return can_i_buy(cost, money, left, mid)
    else:
        return can_i_buy(cost, money, mid + 1, right)


cost, money, right = read_input()
print(can_i_buy(cost, money, 0, right), can_i_buy(cost * 2, money, 0, right), end=' ')
