N_ROWS = 10
N_REPS = 3
LETTERS = 'A L E X S'.split()

for i in range(N_ROWS):
    print(' '.join([lett * N_REPS for lett in LETTERS]))
