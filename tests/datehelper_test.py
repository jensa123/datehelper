"""Unit tests for the datehelper package."""

# pylint: disable=missing-function-docstring,missing-class-docstring

import unittest
from datetime import date
from datehelper import (
    previous_business_day,
    first_day_of_month,
    next_business_day,
    first_day_of_year,
    last_day_of_month,
)


class DateHelperTester(unittest.TestCase):

    def test_previous_business_day(self) -> None:
        dt: date = date(2024, 8, 5)
        prev_bus_day: date = previous_business_day(dt)
        self.assertEqual(date(2024, 8, 2), prev_bus_day)

    def test_first_day_of_month(self) -> None:
        dt: date = date(2024, 8, 5)
        first: date = first_day_of_month(dt)
        self.assertEqual(date(2024, 8, 1), first)

        dt2: date = date(2024, 6, 15)
        first_day_of_june: date = first_day_of_month(dt2)
        first_bus_day_of_june: date = first_day_of_month(
            dt2, business_day=True
        )
        self.assertEqual(date(2024, 6, 1), first_day_of_june)
        self.assertEqual(date(2024, 6, 3), first_bus_day_of_june)

    def test_next_business_day(self) -> None:
        self.assertEqual(date(2024, 8, 5), next_business_day(date(2024, 8, 2)))
        self.assertEqual(date(2024, 8, 2), next_business_day(date(2024, 8, 1)))
        self.assertEqual(date(2024, 8, 5), next_business_day(date(2024, 8, 3)))
        self.assertEqual(date(2024, 8, 5), next_business_day(date(2024, 8, 4)))
        self.assertEqual(date(2024, 8, 6), next_business_day(date(2024, 8, 5)))

    def test_first_day_of_year(self) -> None:
        self.assertEqual(date(2024, 1, 1), first_day_of_year(date(2024, 8, 6)))
        self.assertEqual(
            date(2023, 1, 2),
            first_day_of_year(date(2023, 3, 14), business_day=True),
        )

    def test_last_day_of_month(self) -> None:
        self.assertEqual(
            date(2024, 8, 31), last_day_of_month(date(2024, 8, 6))
        )
        self.assertEqual(
            date(2024, 8, 30),
            last_day_of_month(date(2024, 8, 6), business_day=True),
        )
        self.assertEqual(
            date(2024, 6, 28),
            last_day_of_month(date(2024, 6, 21), business_day=True),
        )
        self.assertEqual(
            date(2024, 6, 30),
            last_day_of_month(date(2024, 6, 21)),
        )


def run_tests():
    unittest.main(module=__name__, verbosity=5)


if __name__ == "__main__":
    run_tests()
