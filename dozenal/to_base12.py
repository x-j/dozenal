# command line usage because why not
import argparse
import notations
import base12

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert a given decimal integer into dozenal.')
    parser.add_argument('int', type=int, help='Decimal integer to be converted.')
    parser.add_argument('-n', required=False, choices=notations.DOZENAL_NOTATIONS_DICT.keys(),
                        help=f'Desired dozenal notation. Default: {base12._DEFAULT_NOTATION}')

    args = parser.parse_args()
    num: base12.Base12Number = base12.convert(vars(args)['int'])
    notation = vars(args)['n']
    if notation and notation != "":
        num.set_notation(notation)
        print(num)
    else:
        print(num)
