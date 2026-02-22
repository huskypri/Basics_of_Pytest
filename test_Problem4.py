import pytest
from Problem4 import filter_temperature_readings
from Problem4 import temperature_readings_order_preserved
from Problem4 import temperature_readings_empty_input_output

def test_temperature_readings():
    assert filter_temperature_readings(readings = [None, 125.01, 40.1, 50.85, 124.0, -40.15, -40.01, None]) == False

def test_temperature_readings_order_preserved():
    assert temperature_readings_order_preserved (readings = [None, 40.1, 50.85, 124.0, -40.15, None]) == [40.1, 50.85, 124.0]

def test_temperature_readings_nonempty_input_output():
    assert temperature_readings_empty_input_output(readings = [None, 40.1, 50.85, 124.0, -40.15, None]) == False

def test_temperature_readings_empty_input_output():
    assert temperature_readings_empty_input_output(readings = []) == True