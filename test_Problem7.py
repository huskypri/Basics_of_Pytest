import pytest
from Problem7 import check_rpm

@pytest.mark.parametrize("rpm_valid, expected", 
    [(801, True),
     (5999, True),
     (4000, True),
    ]
)

def test_check_rpm_valid_rpms(rpm_valid, expected):
        assert check_rpm(rpm_valid) == expected


@pytest.mark.parametrize("rpm_invalid", 
    [
     (799),
     (6001),
    ]
)

def test_check_rpm_invalid_rpms(rpm_invalid):
    with pytest.raises(ValueError):
        check_rpm(rpm_invalid)

