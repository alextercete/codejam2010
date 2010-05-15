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
    if len(sys.argv) > 1:
        input_filename = sys.argv[1]

        input_file = open(input_filename)
        output_file = open(input_filename.replace('.in', '.out'), 'w')

        for i, line in enumerate(input_file):
            if i == 0:
                number_of_inputs = int(line)
            elif i <= number_of_inputs:
                N, K = map(int, line.split())

                snapper_chain = SnapperChain(N)
                lamp_state = snapper_chain.get_lamp_state(K)

                output_file.write('Case #{0}: {1}\n'.format(i, lamp_state))

        input_file.close()
        output_file.close()


if __name__ == '__main__':
    main()
