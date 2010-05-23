import sys

def calculate_intersections(ropes):
    number_of_ropes = len(ropes)
    intersections = 0

    for i in range(number_of_ropes):
        current_rope = ropes[i]
        for j in range(i + 1, number_of_ropes):
            rope = ropes[j]

            if (current_rope[0] > rope[0] and current_rope[1] < rope[1]) \
                    or (rope[0] > current_rope[0] and rope[1] < current_rope[1]):
                intersections += 1

    return intersections


def main(input_file=sys.stdin):
    '''Reads data from standard input, outputs to standard output.'''

    case_number = 0
    next(input_file)  # Go to line 2, 'cause we don't care about the number of cases

    for line in input_file:
        case_number += 1
        N = int(line)
        ropes = []

        for i in range(N):
            next_line = next(input_file)
            A, B = map(int, next_line.split())
            ropes.append((A, B))  # Tuples are faster than lists

        intersections = calculate_intersections(ropes)

        print('Case #{0}: {1}'.format(case_number, intersections))


if __name__ == '__main__':
    main()
