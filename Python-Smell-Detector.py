import tree_sitter
from Detectors.long_parameter_list import detect_long_parameter_list
from Detectors.large_method import detect_long_method
from Detectors.excessive_returns import detect_excessive_returns
from Detectors.code_duplication import detect_duplicate_code
from Detectors.complex_method import detect_complex_method
from Detectors.complex_lambda_function import detect_complex_lambda


def generate_ast(code):
    PYTHON_LANGUAGE = tree_sitter.Language('E:/tree-sitter-python/tree-sitter-python.dll', 'python')
    parser = tree_sitter.Parser()
    parser.set_language(PYTHON_LANGUAGE)
    tree = parser.parse(bytes(code, "utf8"))
    return tree

def detect_code_smells(code):
    tree = generate_ast(code)
    root_node = tree.root_node

    # Threshold for long parameter list smell
    parameter_threshold=3

    # Threshold for excessive return statement smell
    return_threshold=3

    # Threshold for complex method
    max_nesting_level=3
    max_statement_count=10

    # Threshold for complex lambda function smell
    complexity=4 # complexity=num of child+ binary/boolean operators in a lambda

    # Number of Child threshold for Large Method smell
    child_threshold=15


    smells = []

    for node in root_node.children:

        if node.type == 'function_definition':
            # Duplicated Code Smell
            duplicate_code_issues = detect_duplicate_code(node, code)
            for issue in duplicate_code_issues:
                smells.append((issue, 'Duplicate Code'))
            
            # Long Parameter List Smell
            if detect_long_parameter_list(node, parameter_threshold):
                smells.extend([(smell_node, 'Long Parameter List') for smell_node in detect_long_parameter_list(node,parameter_threshold)])
            
            # Excessive Return Smell
            excessive_returns = detect_excessive_returns(node, return_threshold)
            if excessive_returns:
                for return_node in excessive_returns:
                    smells.append((return_node, 'Excessive Returns'))

            # Complex Method Smell
            complex_method_issues = detect_complex_method(node, max_nesting_level, max_statement_count)
            for issue in complex_method_issues:
                smells.append((issue, 'Complex Method'))
            
            # Complex Lambda Functions
            complex_lambda_issues = detect_complex_lambda(node, complexity)
            for issue in complex_lambda_issues:
                smells.append((issue, 'Complex Lambda'))
            
            # Large method smell
            large_method_issues = detect_long_method(node,code, child_threshold)
            for issue in large_method_issues:
                smells.append((issue, 'Large Method'))

    return smells


# Example usage
input_code = """
def calculate_total_price(product_price, quantity, discount, tax):
    if discount:
        total_price = product_price * quantity
        total_price = total_price - (total_price * discount / 100)
    else:
        total_price = product_price * quantity
        tax=product_price*0.1

    if tax:
        tax=product_price*0.1
        total_price = product_price * quantity
        total_price = total_price + (total_price * tax / 100)
    else:
        total_price = product_price * quantity

    return total_price

"""

print(detect_code_smells(input_code))
