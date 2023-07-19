import argparse

# parser = argparse.ArgumentParser(description='My first argument parser')
# parser.add_argument('numbers', metavar='N', type=float, nargs='*', help='press some numbers')
# args = parser.parse_args()
# print(f'В скрипт передано: {args}')


# parser = argparse.ArgumentParser(description='My first argument parser')
# parser.add_argument('numbers', metavar='N', type=float, nargs='*', help='press some numbers')
# args = parser.parse_args()
# print(f'Получили экземпляр Namespace: {args = }')
# print(f'У Namespace работает точечная нотация: {args.numbers = }')
# print(f'Объекты внутри могут быть любыми: {args.numbers[1] = }')


def quadratic_equations(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        return -b / (2 * a)
    return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solving quadratic equations')
    parser.add_argument('param', metavar='a b c', type=float, nargs=3,
                        help='enter a b c separated by a space')
    args = parser.parse_args()
    print(quadratic_equations(*args.param))

