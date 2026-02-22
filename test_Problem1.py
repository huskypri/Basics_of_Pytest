import pytest
from Problem1 import calculate_power

def test_calculate_power_normal_values():
    assert calculate_power(10, 5) == 50
    assert calculate_power(3.5, 2) == 7.0

def test_calculate_power_zero_values():
    assert calculate_power(0, 5) == 0 # Short circuit
    assert calculate_power(10, 0) == 0 # Open circuit

def test_calculate_power_negative_values():
    assert calculate_power(-10, 5) == -50
    assert calculate_power(10, -5) == -50
    assert calculate_power(-10, -5) == 50


# Use of eval is unsafe, so don't use this!
'''@pytest.mark.parametrize("test_input,expected", [("3*5", 15),("2*4", 8),("6*9", 54)])
def test_calculate_power(test_input, expected):
    assert eval(test_input) == expected'''

@pytest.mark.parametrize("voltage,current,expected", 
    [
    (5,2,10),
    (14,2,28), 
    (3.5,2,7),
    (-10,2,-20),
    (0,5,0),
    (10,0,0),
    ]
)
def test_calculate_power_parameterized(voltage, current, expected):
    assert calculate_power(voltage,current) == expected