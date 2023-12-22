import sys
sys.path.append('E:/Code-Smell-Detection')
import pytest
from Detectors.excessive_returns import detect_excessive_returns

class TestNode:
    def __init__(self, type, children=None):
        self.type = type
        self.children = children or []

@pytest.fixture
def block_with_few_returns():
    # A test node representing a block with fewer return statements than the threshold
    return_statements = [TestNode('return_statement') for _ in range(2)]  # 2 return statements
    return TestNode('code_block', children=return_statements)

@pytest.fixture
def block_with_many_returns():
    # A test node representing a block with more return statements than the threshold
    return_statements = [TestNode('return_statement') for _ in range(6)]  # 6 return statements
    return TestNode('code_block', children=return_statements)

def test_detect_block_with_few_returns(block_with_few_returns):
    threshold = 4
    result = detect_excessive_returns(block_with_few_returns, threshold)
    assert result == [], "Block with few returns incorrectly identified as having too many"

def test_detect_block_with_many_returns(block_with_many_returns):
    threshold = 4
    result = detect_excessive_returns(block_with_many_returns, threshold)
    assert len(result) == 6, "Block with many returns not correctly identified"
