import unittest

class Test_monkey_trouble(unittest.TestCase):
    def monkey_trouble(a_smile,b_smile):
        if(a_smile and b_smile):
            return True
        elif(not a_smile and not b_smile):
            return True
        else:
            return False

    def test_monkey1(self):
        self.assertTrue(Test_monkey_trouble.monkey_trouble(True,True))

    def test_monkey2(self):
        self.assertTrue(Test_monkey_trouble.monkey_trouble(False,False))

    def test_monkey3(self):
        self.assertFalse(Test_monkey_trouble.monkey_trouble(True,False))