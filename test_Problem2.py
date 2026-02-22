import pytest
from Problem2 import divide

'''def test_divide_normal_values():
    assert divide(6, 3) == 2
    assert divide(-6, 2) == -3'''

def test_divide_undefined_values(): 
    with pytest.raises(ZeroDivisionError):
        divide(a=19, b=0)


@pytest.mark.parametrize("a,b,expected",
    [
        (10,2,5),
        (15,3,5),
        (20,4,5),
        (-30,0.5,-60),
    ]
)
def test_divide_normal_values(a,b,expected):
    assert divide(a, b) == expected
    