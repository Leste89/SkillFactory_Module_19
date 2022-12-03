from app.calc import Calculator
import pytest

class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_multiply_success(self):
        assert self.calc.multiply(2, 1) == 2
    def test_multiply_unsuccess(self):
        assert self.calc.multiply(2, 1) == 1

    def test_division_success(self):
        assert self.calc.division(2, 1) == 2
    def test_division_unsuccess(self):
        assert self.calc.division(2, 1) == 1
    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1, 0)

    def test_substraction_success(self):
        assert self.calc.substraction(2, 1) == 1
    def test_substraction_unsuccess(self):
        assert self.calc.substraction(2, 1) == 2

    def test_adding_success(self):
        assert self.calc.adding(1, 1) == 2
    def test_adding_unsuccess(self):
        assert self.calc.adding(1, 1) == 3


    def teardown(self):
        print('Выполнение метода Teardown')
