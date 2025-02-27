import sys
import os

# Add the 'src' directory to the sys.path so Python can find it
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from math_operation import add, subtract



# Define the working directory


def test_add():
    result = add(5, 3)
    assert result == 8, f"Expected 8, got {result}"

    result = add(-2, 10)
    assert result == 8, f"Expected 8, got {result}"

def test_subtract():
    result = subtract(10, 5)
    assert result == 5, f"Expected 5, got {result}"

    result = subtract(0, 10)
    assert result == -10, f"Expected -10, got {result}"
    

