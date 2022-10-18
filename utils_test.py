import datetime
import unittest

from utils import generate_pregnancy_weeks


class UtilsTest(unittest.TestCase):

    def test_pregnancy_weeks(self):
        start = datetime.datetime(2022, 8, 12)
        x = generate_pregnancy_weeks(start)
        for w in x:
            print(w)
