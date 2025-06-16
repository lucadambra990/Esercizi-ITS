from my_project.calculator import Calculator

def test_addition():
    calculation:Calculator = Calculator(10,5)
    assert calculation.addition() == 13, 'The sum is wrong'

def test_subtraction():
    calculation:Calculator = Calculator(10,5)
    assert calculation.subtraction() == 5, 'The subtraction in wrong'