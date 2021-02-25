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
        