# Códigos Processo Seletivo TNSI

Files: 

1. Max Difference `max_difference.py`:

```python
'''
Write a code that finds the max difference between two successive elements of the given array after sorting.
'''
class App:
    '''App class'''
    def solve(self, array):
      '''Function than finds the max difference between two successive elements of the given array after sorting '''
      diffs = []
      array.sort()
      for i in range(len(array)-1):
        diff = array[i+1] - array[i]
        diffs.append(diff)
      return max(diffs)

```

2. Name Initials `name_initials.py`:

```python
'''
Write a function which converts names to its initials.
The function should receive a string with forename and surname separated with spaces and 
it should return first letters of these names separated with a single dot.
'''

class App:
    '''
    App Class
    '''
    def makeInitial(self, full_name):
        '''Function which converts names to its initials'''
        names = full_name.split() # Split the names by empty value
        firsts_letters = map(lambda x: x[0], names) # Get the first letter from all names
        return '.'.join(firsts_letters) # Join By dot.

```

3. Numbers_and_strings `numbers_and_strings.py`:

```python
'''
Write a code which sorts the given array containing numbers and strings.
Numbers should be placed first, sorted ascending, and next followed by strings, sorted alphabetically.
All values should maintain their type. 
Also note that numbers written as strings are strings and should be treated as them.
'''
class App:
    '''
    App Class
    '''
    def sort(self, array):
      '''Function that sorts the given array containing numbers and strings'''
      numbers = filter(lambda x: isinstance(x, int), array)
      strings = filter(lambda x: isinstance(x, str), array)
      return sorted(numbers) + sorted(strings)
```

4. (Extra) Tests `tests.py`:


```python

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
```



