import sys

class RollerCoaster:
    '''Represents a theme park roller coaster'''

    def __init__(self, rides_per_day, number_of_seats):
        self.rides_per_day = rides_per_day
        self.number_of_seats = number_of_seats

    def calculate_profit(self, groups):
        profit = 0

        for j in range(self.rides_per_day):

            number_of_people = 0
            for i, group_size in enumerate(groups):

                if number_of_people + group_size <= self.number_of_seats:
                    number_of_people += group_size
                else:
                    break
            
            profit += number_of_people
            groups = groups[i:] + groups[:i]  # Updates the queue for the next ride 

        return profit


def main():
    '''Reads data from standard input, outputs to standard output.
    
    Must call it like this:
    $ python3 script.py < file.in > file.out
    '''
    case_number = 0
    for i, line in enumerate(sys.stdin):
        if i == 0:
            number_of_inputs = int(line)
        else:
            case_number += 1
            R, k, N = map(int, line.split())
            second_line = next(sys.stdin)
            groups = list(map(int, second_line.split()))

            roller_coaster = RollerCoaster(R, k)
            profit = roller_coaster.calculate_profit(groups)

            print('Case #{0}: {1}'.format(case_number, profit))


if __name__ == '__main__':
    main()
