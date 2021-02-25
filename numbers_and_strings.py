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