import pytest
from unittest.mock import Mock, call


def test_call_order_is_correct():
    manager = Mock()

    manager.power_on()
    manager.self_test()
    manager.power_off()

    assert manager.mock_calls == [
        call.power_on(),
        call.self_test(),
        call.power_off(),
    ]


def test_call_order_check_fails_when_order_is_violated():
    manager = Mock()

    manager.self_test()
    manager.power_on()
    manager.power_off()

    expected_order = [
        call.power_on(),
        call.self_test(),
        call.power_off(),
    ]

    with pytest.raises(AssertionError):
        assert manager.mock_calls == expected_order


# Another Solution, which is much more understandable --> 

def test_system_power_sequence():
    power_on = Mock()
    self_test = Mock()
    power_off = Mock()

    power_on()
    self_test()
    power_off()

    assert power_on.mock_calls + self_test.mock_calls + power_off.mock_calls

