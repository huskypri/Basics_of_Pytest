# Basics_of_Pytest
Pytest basics using assert, raises(Error), parametrize, mocking functionality

In this github repository, pytests are created based on problems. All problems are mentioned below: 

Pytest Problems

----- Problem 1: Basic Function Validation ----- 

You are given this function:

def calculate_power(voltage, current):
    return voltage * current
    
Tasks
Write pytest test cases for:
1. normal values
2. zero values
3. negative values
4. Use parametrized tests
Ensure the test file follows pytest naming conventions

----- Problem 2: Exception Handling ----- 

def divide(a, b):
    return a / b

Tasks
1. Write a pytest test to verify:
2. correct division
3. ZeroDivisionError is raised for invalid input
4. Use pytest.raises

----- Problem 3: Log File Validation ----- 

A log file contains voltage readings (one per line):
11.8
12.0
12.7
11.9

Tasks
1. Write a function validate_voltage(log_file_path)
Write pytest tests that:
2. PASS if all values are between 11.5 and 12.5
3. FAIL if any value is outside the range
4. Use temporary files in pytest

----- Problem 4: Sensor Data Quality Check ----- 

def filter_temperature_readings(readings):
    """
    readings: list of float
    returns only valid values
    """

Tasks
1.Invalid values:
- below -40
- above 125
- None
Write pytest tests to verify:
2. invalid values are removed
3. order is preserved
4. empty input returns empty output

----- Problem 5: Mocking Hardware Interface ----- 

class Camera:
    def connect(self):
        pass
    def capture(self):
        pass

Tasks
1. Write pytest tests that:
2. mock connect() and capture()
3. verify capture() is called only after connect()
4. Use unittest.mock

----- Problem 6: Pytest Fixtures (Setup / Teardown) ----- 

You have a database connection class:
class Database:
    def connect(self):
        pass
    def disconnect(self):
        pass

Tasks
Create a pytest fixture that:
1. connects before the test
2. disconnects after the test
3. Write a test that uses this fixture

----- Problem 7: Parameterized Threshold Testing ----- 

def check_rpm(rpm):
    if rpm < 800 or rpm > 6000:
        raise ValueError("RPM out of range")
    return True

Tasks
1. Write parametrized pytest tests for:
- valid RPMs
- invalid RPMs
- Validate both return values and exceptions

----- Problem 8: Stateful System Testing ----- 

class Motor:
    def __init__(self):
        self.running = False
    def start(self):
        self.running = True
    def stop(self):
        self.running = False

Tasks
Write pytest tests to validate:
1. motor starts correctly
2. motor stops correctly
3. motor state transitions are correct

----- Problem 9: Test Report Validation ----- 

Write pytest tests for a function:

def generate_report(results):
    """
    results: list of bool
    returns: dict with pass_count, fail_count
    """

Tasks
1. Test correct counting
2. Test empty input
3. Test invalid input types

----- Problem 10: End-to-End Automation Test ----- 

Simulate a test flow:
def power_on():
    pass

def self_test():
    pass

def power_off():
    pass

Tasks
Write a pytest test that:
1. verifies correct call order
2. fails if order is violated
3. Use mocking
