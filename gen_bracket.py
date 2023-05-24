def gen_binary(control, n1, n2, prefix):
    if n1 == 0 and n2 == 0:
        print(prefix)
    else:
        if n1 > 0:
            gen_binary(control + 1, n1 - 1, n2, prefix + '(')
        if control > 0 and n2 > 0:
            gen_binary(control - 1, n1, n2 - 1, prefix + ')')


def read_input():
    return int(input())


n = read_input()
gen_binary(0, n, n, '')
