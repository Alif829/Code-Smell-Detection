
import sys
sys.path.append('E:/Code-Smell-Detection')
import pytest
from Detectors.large_method import detect_long_method

class TestNode:
    def __init__(self, children):
        self.children = children

@pytest.fixture
def small_method_node():
    # A test node representing a method with fewer children than the threshold
    return TestNode(children=[TestNode([]) for _ in range(3)])  # 3 children

@pytest.fixture
def large_method_node():
    # A test node representing a method with more children than the threshold
    return TestNode(children=[TestNode([]) for _ in range(6)])  # 6 children

def test_detect_small_method(small_method_node):
    threshold = 5
    result = detect_long_method(small_method_node, "code", threshold)
    assert result == [], "Small method incorrectly identified as large"

def test_detect_large_method(large_method_node):
    threshold = 5
    result = detect_long_method(large_method_node, "code", threshold)
    assert result == [large_method_node], "Large method not correctly identified"
