from src.c11.tiy_11_3 import Employee
import pytest


# def test_give_default_raise():
#     employee = Employee('Tanvir', 'Anjum', 4000)
#     employee.give_raise()
#     assert employee.salary == 9000


# def test_give_custom_raise():
#     employee = Employee('Tanvir', 'Anjum', 5000)
#     employee.give_raise(10000)
#     assert employee.salary == 15000


@pytest.fixture
def employee():
    return Employee('Tanvir', 'Anjum', 5000)


def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.salary == 10000


def test_give_custom_raise(employee):
    employee.give_raise(10000)
    assert employee.salary == 15000
