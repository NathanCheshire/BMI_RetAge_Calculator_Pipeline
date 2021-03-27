import Functions
import math
import sys
import unittest

##AUTOMATED TESTS##############################

class UnitTester(unittest.TestCase):

    def setUp(self):
        print("Unit test setup")
        pass
    def tearDown(self):
        print("unit test teardown")
        pass
    

##MANUAL TESTS#################################

class TestFunctions(unittest.TestCase):
    def test_bmiCalculation(self):
        assert math.isclose(Functions.getBMI(5,9,141),21.323, rel_tol = 0.001)
        assert math.isclose(Functions.getBMI(4,11,150),31.026, rel_tol = 0.001)
        assert math.isclose(Functions.getBMI(6,2,195),25.639, rel_tol = 0.001)
        
    def test_bmiCategory(self):
        assert Functions.getBMICategory(16.0) == "underweight"
        assert Functions.getBMICategory(18.4) == "underweight"
        assert Functions.getBMICategory(18.5) == "normal"
        assert Functions.getBMICategory(18.6) == "normal"
        assert Functions.getBMICategory(24.9) == "normal"
        assert Functions.getBMICategory(25.0) == "overweight"
        assert Functions.getBMICategory(25.1) == "overweight"
        assert Functions.getBMICategory(29.9) == "overweight"
        assert Functions.getBMICategory(30.0) == "obese"
        assert Functions.getBMICategory(30.1) == "obese"
        assert Functions.getBMICategory(50.0) == "obese"

    def test_retirementAgeCalculation(self):
        assert math.isclose(Functions.getRetirementAge(25,65000,10,1500000),  96, rel_tol = 0)
        assert math.isclose(Functions.getRetirementAge(45,100000,15,500000), 70, rel_tol = 0)
        assert math.isclose(Functions.getRetirementAge(10,100000,12,700000), 54, rel_tol = 0)
        assert math.isclose(Functions.getRetirementAge(20,0,50,600000), sys.maxsize, rel_tol = 0)
        assert math.isclose(Functions.getRetirementAge(60,1,0,3000000), sys.maxsize, rel_tol = 0)
        assert math.isclose(Functions.getRetirementAge(80,100000,100,0), 80, rel_tol = 0)
        assert math.isclose(Functions.getRetirementAge(100,50,57,1000000), 26091, rel_tol = 0)

    def test_retirementAgeCategory(self):
        assert Functions.getRetirementCategory(70.0) == "will meet"
        assert Functions.getRetirementCategory(99.0) == "will meet"
        assert Functions.getRetirementCategory(99.9) == "will meet"
        assert Functions.getRetirementCategory(100.0) == "will not meet"
        assert Functions.getRetirementCategory(100.1) == "will not meet"
        assert Functions.getRetirementCategory(150.0) == "will not meet"
