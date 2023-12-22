import sys
sys.path.append('E:/Code-Smell-Detection')
import pytest
from Detectors.complex_lambda_function import detect_complex_lambda

class TestNode:
    def __init__(self, type, children=None):
        self.type = type
        self.children = children or []

@pytest.fixture
def simple_lambda_node():
    # A test node representing a simple lambda with low complexity
    return TestNode('lambda', children=[TestNode('some_expression')])

@pytest.fixture
def complex_lambda_node():
    # A test node representing a complex lambda with high complexity
    binary_ops = [TestNode('binary_operator') for _ in range(3)]
    child_nodes = [TestNode('some_expression') for _ in range(4)] + binary_ops
    return TestNode('lambda', children=child_nodes)

def test_detect_simple_lambda(simple_lambda_node):
    complexity_threshold = 4
    result = detect_complex_lambda(simple_lambda_node, complexity_threshold)
    assert result == [], "Simple lambda incorrectly identified as complex"

def test_detect_complex_lambda(complex_lambda_node):
    complexity_threshold = 4
    result = detect_complex_lambda(complex_lambda_node, complexity_threshold)
    assert len(result) > 0, "Complex lambda not correctly identified"
