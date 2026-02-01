import numpy as np
import torch
import pytest

def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:

        def f():
            pass

        f()
    assert "maximum recursion" in str(excinfo.value)

if __name__ == '__main__':
    pytest.main()