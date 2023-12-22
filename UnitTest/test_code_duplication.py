import sys
sys.path.append('E:/Code-Smell-Detection')
import pytest
from Detectors.code_duplication import detect_duplicate_code

class TestNode:
    def __init__(self, type, start_byte, end_byte, children=None):
        self.type = type
        self.start_byte = start_byte
        self.end_byte = end_byte
        self.children = children or []

@pytest.fixture
def ast_with_duplicate_code():
    # Creating test nodes representing duplicate expression statements
    expr1 = TestNode('expression_statement', 0, 10)
    expr2 = TestNode('expression_statement', 20, 30)
    expr3 = TestNode('expression_statement', 40, 50)  # Duplicate of expr1
    root = TestNode('root', 0, 50, children=[expr1, expr2, expr3])
    return root

def test_detect_duplicate_code(ast_with_duplicate_code):
    # Simulated code corresponding to the AST nodes
    code = "a = 1\nb = 2\na = 1"
    duplicates = detect_duplicate_code(ast_with_duplicate_code, code)
    assert len(duplicates) > 1, "Duplicate code not correctly identified"
    assert all(node.type == 'expression_statement' for node, _ in duplicates), "Non-expression statement incorrectly marked as duplicate"

