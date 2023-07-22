import argparse


def fibonachi(num):
    fib = []
    for i in range(1, num):
        if i == 1:
            fib.append(i)
        elif i == 2:
            fib.append(i)
        else:
            fib.append(fib[i - 3] + fib[i - 2])
    return fib


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='For fibonachi')
    parser.add_argument('fibonachi', metavar='Number', nargs=1, type=int, help='Enter integer number')
    args = parser.parse_args()
    print(fibonachi(*args.fibonachi))
