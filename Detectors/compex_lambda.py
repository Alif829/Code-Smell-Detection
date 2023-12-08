import tree_sitter


def _count_operators(node):
    operator_count = 0
    for child in node.children:
        if child.type in ["binary_operator", "comparison_operator", "boolean_operator"]:
            operator_count += 1
        elif child.type != "lambda":
            operator_count += _count_operators(child)
    return operator_count


def _get_nested_depth(node):
    nested_depth = 0
    for child in node.children:
        if child.type == "lambda":
            nested_depth = max(nested_depth, _get_nested_depth(child) + 1)
    return nested_depth


def detect_complex_lambda(node, average_lambda_complexity):
    complex_lambdas = []

    def _check_complexity(lamb_node):
        # Check for complex expressions (operator count)
        operator_count = _count_operators(lamb_node)
        if operator_count > 2:
            complex_lambdas.append(lamb_node)

        # Check for complex nested expressions (operator count and depth)
        nested_depth = _get_nested_depth(lamb_node)
        if nested_depth > 1 and operator_count > 1:
            complex_lambdas.append(lamb_node)

        # Check for child expressions (recursive)
        for child in lamb_node.children:
            if child.type != "lambda":
                _check_complexity(child)

    for child in node.children:
        if child.type == "lambda":
            _check_complexity(child)

    return complex_lambdas

