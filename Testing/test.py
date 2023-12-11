import unittest
import main #we import the functions to be tested in the main module

class TestMain(unittest.TestCase): #inside the class we inherit TestCase from unittest module we imported.
    def setUp(self) -> None:
        print('About to test functions')

    def test_do_stuff(self):
        '''Testing if the function works well'''
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'hehe'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError) #in the event that we pass a string, do we get a ValueError?

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number.') #in the event that we pass a string, do we get a ValueError?

    def tearDown(self) -> None:
        print('Done with the test.')
        
if __name__ == '__main__':
    unittest.main() 