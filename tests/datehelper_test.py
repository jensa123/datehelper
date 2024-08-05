"""Unit tests for the datehelper package."""

# pylint: disable=missing-function-docstring,missing-class-docstring

import unittest
from datetime import date
from datehelper import previous_business_day, first_day_of_month


class DateHelperTester(unittest.TestCase):

    def test_previous_business_day(self) -> None:
        dt: date = date(2024, 8, 5)
        prev_bus_day: date = previous_business_day(dt)
        self.assertEqual(date(2024, 8, 2), prev_bus_day)

    def test_first_day_of_month(self) -> None:
        dt: date = date(2024, 8, 5)
        first: date = first_day_of_month(dt)
        self.assertEqual(date(2024, 8, 1), first)
