import sys

LAMP_STATE_ON = 'ON'
LAMP_STATE_OFF = 'OFF'

class SnapperChain:
    '''Represents a chain of connected snappers'''

    def __init__(self, number_of_snappers):
        self.number_of_snappers = number_of_snappers

    def get_lamp_state(self, number_of_snaps):
        if number_of_snaps > 0 and \
                (number_of_snaps + 1) % (2 ** self.number_of_snappers) == 0:
            return LAMP_STATE_ON
        return LAMP_STATE_OFF


def main():
    '''Reads data from standard input, outputs to standard output.
    
    Must call it like this:
    $ python3 script.py < file.in > file.out
    '''
    for i, line in enumerate(sys.stdin):
        if i == 0:
            number_of_inputs = int(line)
        elif i <= number_of_inputs:
            N, K = map(int, line.split())

            snapper_chain = SnapperChain(N)
            lamp_state = snapper_chain.get_lamp_state(K)

            print('Case #{0}: {1}'.format(i, lamp_state))


if __name__ == '__main__':
    main()
