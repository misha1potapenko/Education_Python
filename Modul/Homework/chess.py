from random import randint

amount = 4
for_amount = 5


def are_queens_attacking_each_other(queens: list(tuple())):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if queens[i][0] == queens[j][0] or \
                    queens[i][1] == queens[j][1] or \
                    abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return False
    return True


def position_generation() -> list:
    result = []
    queens = []
    count = 0

    while count != amount:
        for _ in range(for_amount):
            queens.append((randint(1, 8), randint(1, 8)))
        if are_queens_attacking_each_other(queens):
            result.append(queens)
            count += 1
        queens = []

    return result


if __name__ == '__main__':
    for i, value in enumerate(position_generation(), 1):
        print(f'{i} - {value}')
