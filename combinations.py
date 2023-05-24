KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def combinations(buttons, path, result):
    if buttons == '':
        result.append(path)
        return
    for letter in KEYBOARD[buttons[0]]:
        path += letter
        combinations(buttons[1:], path, result)
        path = path[:-1]


def read_input():
    return input()


def main():
    buttons = read_input()
    result = []
    combinations(buttons, '', result)
    print(*result)


if __name__ == '__main__':
    main()

