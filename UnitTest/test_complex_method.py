import sys
sys.path.append('E:/Code-Smell-Detection')
import pytest
from Detectors.complex_method import detect_complex_method

class TestNode:
    def __init__(self, type, children=None):
        self.type = type
        self.children = children or []

@pytest.fixture
def simple_method_node():
    # A test node representing a simple method within the allowed nesting level and statement count
    nested_statements = [TestNode('if_statement', [TestNode('some_statement')]) for _ in range(2)]  # 2 nested statements
    return TestNode('method', children=nested_statements)

@pytest.fixture
def complex_method_node():
    # A test node representing a complex method exceeding the allowed nesting level or statement count
    deeply_nested_statements = [TestNode('if_statement', [TestNode('for_statement', [TestNode('some_statement')])]) for _ in range(3)]  # 3 deeply nested statements
    return TestNode('method', children=deeply_nested_statements)

def test_detect_simple_method(simple_method_node):
    max_nesting_level = 2
    max_statement_count = 4
    result = detect_complex_method(simple_method_node, max_nesting_level, max_statement_count)
    assert result == [], "Simple method incorrectly identified as complex"

def test_detect_complex_method(complex_method_node):
    max_nesting_level = 2
    max_statement_count = 4
    result = detect_complex_method(complex_method_node, max_nesting_level, max_statement_count)
    assert len(result) > 0, "Complex method not correctly identified"


