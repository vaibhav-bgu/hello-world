# content of test_class.py
import numpy as np
import torch
import pytest
from typing import List

def test_floats():
    assert (0.1 + 0.2) == pytest.approx(0.4)


def test_arrays():
    a = np.array([1.0, 2.0, 3.0])
    b = np.array([0.9999, 2.0001, 3.0])
    assert a == pytest.approx(b)

def fn1(x: List, y: int):
    return y in x

a = torch.zeros(2,2)
print("my tensor is ", fn1([3,4], 3))