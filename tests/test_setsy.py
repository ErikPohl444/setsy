from src.setsy import setsy
import pytest


def test_powerset():
    x = setsy(["1", "2", "3"])
    y = x.powerset()
    expected = [
                ('1', '2'),
                ('3',),
                ('1',),
                ('3', '2'),
                ('2',),
                ('1', '3'),
                ('1', '3', '2'),
                ()
            ]
    for item in y:
        print(item)
        assert set(item) in [
            set(n) for n in expected
        ]
    assert len(y) == len(expected)
