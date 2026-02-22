import pytest
from Problem3 import validate_voltage


def test_validate_voltage_passes_when_all_values_in_range(tmp_path):
    log_file = tmp_path / "voltage.log"
    log_file.write_text("11.8\n12.0\n12.5\n11.5\n", encoding="utf-8")

    assert validate_voltage(log_file) is True


def test_validate_voltage_fails_when_any_value_out_of_range(tmp_path):
    log_file = tmp_path / "voltage.log"
    log_file.write_text("11.8\n12.7\n11.9\n", encoding="utf-8")

    assert validate_voltage(log_file) is False
