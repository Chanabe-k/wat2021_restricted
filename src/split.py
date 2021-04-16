import sys

if len(sys.argv) != 3:
    print('Usage: split.py NUM FILE', file=sys.stderr)
    print('Output NUM pieces of FILE to FILE.0, FILE.1, ...', file=sys.stderr)
    sys.exit()

n_parts = int(sys.argv[1])
n_digits = len(str(n_parts))
file = sys.argv[2]

n_lines = sum(1 for _ in open(file))

def divide(num, n_parts):
    """Divide a number into `n_parts`
    
    >>> divide(10, 3)
    [4, 3, 3]
    """
    q, r = divmod(num, n_parts)
    ret = [q] * n_parts
    for i in range(r):
        ret[i] += 1
    return ret

n_lines_per_file = divide(n_lines, n_parts)

with open(file) as fi:
    for i, n in enumerate(n_lines_per_file):
        suffix = str(i).zfill(n_digits)
        with open(f'{file}.{suffix}', 'w') as fo:
            for _ in range(n):
                fo.write(fi.readline())
