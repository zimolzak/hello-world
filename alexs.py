N_ROWS = 10
N_REPS = 3

LETTERS = 'A L E X S'.split()

for i in range(N_ROWS):
    for L in LETTERS:
        for j in range(N_REPS):
            print(L, end='')
        print(' ', end='')
    print()
