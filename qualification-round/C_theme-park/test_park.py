import unittest
from park import RollerCoaster

class TestRollerCoaster(unittest.TestCase):

    def test_1_group_with_lonely_person(self):
        self.check_roller_coaster_profit(3, 3, 5, [1])

    def test_1_group_with_5_people(self):
        self.check_roller_coaster_profit(15, 3, 5, [5])

    def test_5_seats_2_groups_with_4_people_each(self):
        self.check_roller_coaster_profit(12, 3, 5, [4, 4])

    def test_4_rides_6_seats_4_groups(self):
        self.check_roller_coaster_profit(21, 4, 6, [1, 4, 2, 1])

    def test_100_rides_10_seats_1_group_with_lonely_person(self):
        self.check_roller_coaster_profit(100, 100, 10, [1])

    def test_5_rides_5_seats_10_groups(self):
        self.check_roller_coaster_profit(20, 5, 5, [2, 4, 2, 3, 4, 2, 1, 2, 1, 3])

    def xtest_extreme_inputs(self):
        self.check_roller_coaster_profit(2 * 10 ** 8, 10 ** 8, 2, [2]) 

    def check_roller_coaster_profit(self, profit, rides_per_day, number_of_seats, groups):
        roller_coaster = RollerCoaster(rides_per_day, number_of_seats)
        self.assertEquals(profit, roller_coaster.calculate_profit(groups))


if __name__ == '__main__':
    unittest.main()
