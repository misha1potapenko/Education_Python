import guess
import sys
init_numbers = list(map(int, [i for i in sys.argv][1:]))
guess.guess_f(*init_numbers)