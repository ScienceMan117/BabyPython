import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis','joplin')
# A unittest function that verifies a result recieved matches the result you
# expected to see.        
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
        
unittest.main()

# Example of an error error message that is given when test fails.
"""
E
======================================================================
ERROR: test_first_last_name (__main__.NamesTestCase)
Do names like 'Janis Joplin' work?
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_name_function.py", line 9, in test_first_last_name
    formatted_name = get_formatted_name('janis','joplin')
TypeError: get_formatted_name() missing 1 required positional argument: 'last'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)


------------------
"""
