
import re

def detect_inconsistent_naming(node, code):
    variable_pattern = re.compile(r"\b([A-Z][a-z0-9]+|[a-z0-9]+[A-Z]|[a-zA-Z]{1})\b")
    smells = []

    # If current node is an expression_statement, check its naming pattern
    if node.type == 'expression_statement':
        node_code = code[node.start_byte:node.end_byte]
        if variable_pattern.search(node_code):
            smells.append(node)

    # Check children nodes
    for child in node.children:
        smells.extend(detect_inconsistent_naming(child, code))

    return smells



