import unittest

class TestSleepIn(unittest.TestCase):
    def sleep_in(weekday, vacation):
        if (vacation or not weekday):
            return True
        else:
            return False


    def test_sleepIn1(self):
        self.assertTrue(TestSleepIn.sleep_in(False, False))
