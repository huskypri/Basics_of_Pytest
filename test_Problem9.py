import pytest
from Problem9 import generate_report


def test_generate_report_correct_counting(results = [0,1,0,1,0,1,1,1,1,0,0,0,1,1,1]):
    dict ={"pass_count": 0, "fail_count": 0}
    for result in results:
        if result == 1:
            dict["pass_count"] = dict["pass_count"] + 1
        else:
            dict["fail_count"] = dict["fail_count"] + 1

    assert dict["pass_count"] == 9
    assert dict["fail_count"] == 6


def test_generate_report_empty_input(results = []):
    dict ={"pass_count": 0, "fail_count": 0}
    if len(results) == 0:
        assert dict["pass_count"] == 0
        assert dict["fail_count"] == 0


def test_generate_report_invalid_input_type(results = [0,1,'x','&',0,1,'a',1,'v',0,0,0,'0',1,1]):
    dict ={"pass_count": 0, "fail_count": 0}
    test_result_valid = 'Valid'
    test_result_invalid = 'Invalid'
    for result in results:
        if isinstance(result, str):
            assert test_result_invalid == 'Invalid'
        else: 
            assert test_result_valid == 'Valid'

"""3 tests will pass, but right now they are not actually validating generate_report yet.

Big hint:

Each test should call generate_report(...) and assert on its returned value or raised error.
Your current tests mostly validate local variables (dict, test_result_valid) that are created inside the test, so they would still pass 
even if generate_report is wrong or unimplemented.
For “correct counting,” think in terms of input list -> expected pass_count and fail_count from the function output.
For “empty input,” decide expected behavior clearly: should it return zeros or raise? Then assert exactly that behavior.
For “invalid input types,” define one rule first (reject non-bool values, or coerce them), then test that rule consistently. 
Right now strings are checked, but the function behavior for invalid values is never verified."""

# Additional tests appended below existing tests (original tests unchanged)
def test_generate_report_correct_counting_calls_function():
    results = [True, False, True, True, False]
    report = generate_report(results)
    assert report == {"pass_count": 3, "fail_count": 2}


def test_generate_report_empty_input_calls_function():
    report = generate_report([])
    assert report == {"pass_count": 0, "fail_count": 0}


def test_generate_report_invalid_input_types_calls_function():
    with pytest.raises(TypeError):
        generate_report([True, "x", False])


"""The added last three testcases will fail because generate_report() currently returns None and does not raise TypeError for invalid entries."""