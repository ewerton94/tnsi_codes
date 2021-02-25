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