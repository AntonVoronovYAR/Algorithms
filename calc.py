from typing import List

OPERATIONS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y
}


def read_input() -> List:
    """Считываем входные данные."""
    return [i for i in input().split()]


def check(digit1: str, digit2: str, operand: str) -> bool:
    """
    Проверка последовательности значений на соответствие.

    (число - число - операция)
    """
    return (digit1.lstrip("-").isdigit() and
            digit2.lstrip("-").isdigit() and not
            operand.lstrip("-").isdigit())


def solution(string: List) -> List:
    """Основная функция вычислений."""
    start_index: int = 0
    while len(string) > 2:
        digit1 = string[start_index]
        digit2 = string[start_index+1]
        operand = string[start_index+2]
        if check(digit1, digit2, operand):
            result = OPERATIONS[operand](int(digit1), int(digit2))
            del string[start_index:start_index+3]
            string.insert(start_index, str(result))
            start_index = 0
        else:
            start_index += 1
    return string


if __name__ == "__main__":
    result = solution(read_input())
    if len(result) == 1:
        print(*result)
    else:
        print(result[-1])
