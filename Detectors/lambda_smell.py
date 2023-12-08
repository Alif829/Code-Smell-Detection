def detect_complex_lambda(node, code):
    smells = []
    complexity_threshold = 1  # Threshold for the number of expressions

    # Count the number of expressions within the lambda
    expression_count = sum(1 for child in node.children if child.type == 'expression')

    if expression_count > complexity_threshold:
        smells.append((node, 'Complex Lambda Function'))

    # Detect nested structures within the lambda
    for child in node.children:
        if child.type in ['if_expression', 'for_expression', 'while_expression']:
            smells.append((node, 'Complex Lambda Function (Nested Structures)'))
            break

    return smells