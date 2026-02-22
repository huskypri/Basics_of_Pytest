"""Validate voltage readings from a log file."""

def validate_voltage(log_file_path):
    """Return True when every voltage value is between 11.5 and 12.5 (inclusive)."""
    with open(log_file_path, "r", encoding="utf-8") as file:
        for line in file:
            stripped = line.strip()
            if not stripped:
                continue
            value = float(stripped)
            if value < 11.5 or value > 12.5:
                return False
    return True
