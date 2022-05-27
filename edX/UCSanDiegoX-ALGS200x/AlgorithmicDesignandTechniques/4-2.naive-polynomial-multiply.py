from dataclasses import dataclass


def superscript(n):
    return "".join(["⁰¹²³⁴⁵⁶⁷⁸⁹"[ord(c)-ord('0')] for c in str(n)])


@dataclass
class Polynomial:
    a: tuple

    def __str__(self, ) -> str:
        _str = ''
        n = len(self.a)
        for idx, term in enumerate(self.a):
            if idx > 0:
                if term < 0:
                    _str += '- '
                else:
                    _str += '+ '
            x = f'x{superscript(n-idx-1)}'
            if n-idx-1 == 0:
                x = ''
            elif n-idx-1 == 1:
                x = 'x'
            _str += f'{term}{x} '
        return _str


def poly_multiply(n, a, b):
    '''
    Multiply passed polynomials
    Args:
        n (int): order of the (higher) polynomial
        a (tuple): coefficients of first polynomial\
            e.g. 3x^2 + 2x + 5 would be represented as\
                (3, 2, 5)
        b (tuple): coefficients of second polynomial
    Returns:
        product (tuple)
    '''
    a_p = Polynomial(a)
    b_p = Polynomial(b)
    print(a_p)
    print(b_p)
    _result_dct = {}
    for a_pos, a_term in enumerate(a_p.a):
        a_exp = len(a_p.a) - a_pos - 1
        for b_pos, b_term in enumerate(b_p.a):
            b_exp = len(b_p.a) - b_pos - 1
            if (a_exp + b_exp) not in _result_dct:
                _result_dct[(a_exp + b_exp)] = 0
            _result_dct[(a_exp + b_exp)] += (a_term * b_term)
    _result_lst = []
    for _k, _v in _result_dct.items():
        _result_lst.append(_v)
    return tuple(_result_lst)


def main():
    n = 3
    a = (3, 2, 5)
    b = (5, 1, 2)
    o = poly_multiply(n, a, b)
    assert o == (15, 13, 33, 9, 10)


if __name__ == '__main__':
    main()
