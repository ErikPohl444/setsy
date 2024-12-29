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


def test_is_not_subset():
    s1 = setsy([1, 2, 3])
    s2 = setsy([1, 2, 4, 5])
    assert s1.is_not_subset(s2)


def test_is_not_superset():
    s1 = setsy([1, 2, 3])
    s2 = setsy([1, 2, 4, 5])
    assert s2.is_not_superset(s1)


def test_preserve_order():
    l1 = [8, 6, 4, 3, 5, 7, 2, 1]
    s1 = setsy(l1)
    s1.printorig()
    assert s1.iter == l1
