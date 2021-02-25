
import unittest
from max_difference import App as MaxDifferenceApp
from name_initials import App as NameInitialsApp
from numbers_and_strings import App as NumbersAndStringsApp

class TestMaxDifference(unittest.TestCase):
    def test1(self):
        app = MaxDifferenceApp()
        self.assertEqual(app.solve([132,64,12,64,22,75]), 57)
    def test2(self):
        app = MaxDifferenceApp()
        self.assertEqual(app.solve([5,23,75,23,75]), 52)

class TestNameInitials(unittest.TestCase):
    def test1(self):
        app = NameInitialsApp()
        self.assertEqual(app.makeInitial('Joseph Stalin'), "J.S")
    def test2(self):
        app = NameInitialsApp()
        self.assertEqual(app.makeInitial('Elisabeth Smith'), "E.S")
    def test3(self):
        app = NameInitialsApp()
        self.assertEqual(app.makeInitial('Amy Johnson'), "A.J")

class TestNumbersAndStrings(unittest.TestCase):
    def test1(self):
        app = NumbersAndStringsApp()
        self.assertEqual(app.sort([1,3,'123','dsd','ghr',99]), [1, 3, 99, "123", "dsd", "ghr"])
    def test2(self):
        app = NumbersAndStringsApp()
        self.assertEqual(app.sort(['14',43,'76',23,'adadsd','xghr','saaa']), [23, 43, "14", "76", "adadsd", "saaa", "xghr"])

if __name__ == '__main__':
    unittest.main()