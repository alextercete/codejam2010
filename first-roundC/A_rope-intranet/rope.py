import sys

def calculate_intersections(ropes):
    number_of_ropes = len(ropes)
    intersections = set()

    for i in range(number_of_ropes):
        current_rope = ropes[i]
        for j in range(i + 1, number_of_ropes):
            rope = ropes[j]

            if (current_rope[0] > rope[0] and current_rope[1] < rope[1]) \
                    or (rope[0] > current_rope[0] and rope[1] < current_rope[1]):
                pair = [''.join(map(str, current_rope)), ''.join(map(str, rope))]
                intersections.add(''.join(sorted(pair)))

    return len(intersections)


def main():
    '''Reads data from standard input, outputs to standard output.
    
    Must call it like this:
    $ python3 script.py < file.in > file.out
    '''
    number_of_lines = int(sys.stdin.readline())
    case_number = 0

    for line in sys.stdin:
        N = int(line)
        case_number += 1
        ropes = []

        for i in range(N):
            next_line = next(sys.stdin)
            ropes.append(list(map(int, next_line.split())))

        intersections = calculate_intersections(ropes)

        print('Case #{0}: {1}'.format(case_number, intersections))


if __name__ == '__main__':
    main()
