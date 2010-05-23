import unittest
from rope import calculate_intersections

class TestRope(unittest.TestCase):

    def test_one_rope_no_intersections(self):
        ropes = [[1, 3]]
        self.assertEquals(0, calculate_intersections(ropes))

    def test_two_ropes_no_intersections(self):
        ropes = [[2, 2], [3, 5]]
        self.assertEquals(0, calculate_intersections(ropes))

    def test_three_ropes_no_intersections(self):
        ropes = [[1, 1], [2, 3], [4, 5]]
        self.assertEquals(0, calculate_intersections(ropes))

    def test_two_ropes_one_intersection(self):
        ropes = [[1, 2], [2, 1]]
        self.assertEquals(1, calculate_intersections(ropes))

    def test_another_two_ropes_one_intersection(self):
        ropes = [[2, 10], [3, 1]]
        self.assertEquals(1, calculate_intersections(ropes))

    def test_three_ropes_two_intersections(self):
        ropes = [[1, 10], [5, 5], [7, 7]]
        self.assertEquals(2, calculate_intersections(ropes))


if __name__ == '__main__':
    unittest.main()
