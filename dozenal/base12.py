from notations import get_notation, NotationSystem

# Base12 conversion code from someone on /r/dozenal
# todo: find out who exactly

_DEFAULT_NOTATION = 'ascii'



class Base12Number:
    notation: NotationSystem

    def __init__(self, val, notation: str = _DEFAULT_NOTATION):
        self.val = val
        self.notation = get_notation(notation)

        if not isinstance(val, str):
            # obtaining val == str means we will convert from hex.... i think?
            raise TypeError(f"Base12Number expected str, got {type(val)}")

    def __str__(self):
        return self.val.replace('a', self.notation.DEC_SYMBOL).replace('b', self.notation.EL_SYMBOL)

    def set_notation(self, new_n):
        self.notation = get_notation(new_n)


def convert_to_base12(n, notation=_DEFAULT_NOTATION):
    q = -1
    res = ''

    if n < 0:
        raise TypeError("Only positive ints for now, please.")

    if isinstance(n, int):
        while q != 0:
            q = n // 12
            r = n % 12
            res = hex(r)[2:] + res
            n = q
    elif isinstance(n, float):
        raise TypeError("Only positive ints for now, please.")

    return Base12Number(res, notation)


def __f(x, dec):
    y = x * (12 ** dec)

    return convert_to_base12(int(y))


def __raccord(str):
    res = str[0] + ","

    for i in range(1, len(str)):
        res += str[i]

    return res


convert = convert_to_base12












