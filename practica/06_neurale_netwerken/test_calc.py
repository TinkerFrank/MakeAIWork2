import unittest
import calc 

class TestCalc(unittest.TestCase):

    def setUp(self):
        # define test variables to be used in every test, for example:
        self.emp_1 = Employee('Tom','Davids', 5000)
        self.emp_2 = Employee('Carol','Richards', 5000)


    def tearDown(self):
        pass

    def test_add(self): #only functions that start with 'test' will run
        result = calc.add(10,5)
        self.assertEqual(result,15)
        self.assertEqual(calc.add(-1,1),0)
        self.assertEqual(calc.add(-1,-1),-2)

    def test_multiply(self): 
        result = calc.multiply(10,5)
        self.assertEqual(result,50)
        self.assertEqual(calc.multiply(-1,1),-1)
        self.assertEqual(calc.multiply(-1,-1),1)

    def test_divide(self): 
        result = calc.divide(10,5)
        self.assertEqual(result,2)
        self.assertEqual(calc.divide(-1,1),-1)
        self.assertEqual(calc.divide(-1,-1),1)

# in order to run it directly, otherwise:
# 'python -m unittest test_calc.py'
if __name__ == '__main__':
    unittest.main()

