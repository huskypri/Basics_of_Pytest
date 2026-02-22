"""Parameterized Threshold Testing"""

def check_rpm(rpm):
    if rpm < 800 or rpm > 6000:
        raise ValueError("RPM out of range")
    return True
