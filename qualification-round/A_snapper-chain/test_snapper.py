import unittest
from snapper import SnapperChain, LAMP_STATE_ON, LAMP_STATE_OFF

class TestSnapper(unittest.TestCase):

    def test_1_snapper_no_snaps(self):
        self.check_lamp_state(LAMP_STATE_OFF, 1, 0)

    def test_1_snapper_1_snap(self):
        self.check_lamp_state(LAMP_STATE_ON, 1, 1)

    def test_2_snappers_2_snaps(self):
        self.check_lamp_state(LAMP_STATE_OFF, 2, 2)

    def test_2_snappers_3_snaps(self):
        self.check_lamp_state(LAMP_STATE_ON, 2, 3)

    def test_3_snappers_14_snaps(self):
        self.check_lamp_state(LAMP_STATE_OFF, 3, 14)

    def test_3_snappers_15_snaps(self):
        self.check_lamp_state(LAMP_STATE_ON, 3, 15)

    def test_4_snappers_no_snaps(self):
        self.check_lamp_state(LAMP_STATE_OFF, 4, 0)

    def test_4_snappers_47_snaps(self):
        self.check_lamp_state(LAMP_STATE_ON, 4, 47)

    def check_lamp_state(self, lamp_state, number_of_snappers, number_of_snaps):
        snapper_chain = SnapperChain(number_of_snappers)

        self.assertEquals(lamp_state, snapper_chain.get_lamp_state(number_of_snaps))


if __name__ == '__main__':
    unittest.main()
