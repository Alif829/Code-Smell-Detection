import sys
sys.path.append('E:/Code-Smell-Detection')
import pytest
from Detectors.long_parameter_list import detect_long_parameter_list

class TestNode:
    def __init__(self, type, children=None):
        self.type = type
        self.children = children or []

@pytest.fixture
def method_with_few_parameters():
    # A test node representing a method with fewer parameters than the threshold
    parameters = [TestNode('identifier') for _ in range(3)]  # 3 parameters
    parameters_node = TestNode('parameters', children=parameters)
    return TestNode('function_definition', children=[parameters_node])

@pytest.fixture
def method_with_many_parameters():
    # A test node representing a method with more parameters than the threshold
    parameters = [TestNode('identifier') for _ in range(7)]  # 7 parameters
    parameters_node = TestNode('parameters', children=parameters)
    return TestNode('function_definition', children=[parameters_node])

def test_detect_method_with_few_parameters(method_with_few_parameters):
    threshold = 5
    result = detect_long_parameter_list(method_with_few_parameters, threshold)
    assert result == [], "Method with few parameters incorrectly identified as having too many"

def test_detect_method_with_many_parameters(method_with_many_parameters):
    threshold = 5
    result = detect_long_parameter_list(method_with_many_parameters, threshold)
    assert len(result) == 7, "Method with many parameters not correctly identified"
