import tree_sitter

from generate_ast import generate_ast

from Detectors.long_parameter_list import detect_long_parameter_list
from Detectors.large_method import detect_long_method
from Detectors.excessive_returns import detect_excessive_returns
from Detectors.code_duplication import detect_duplicate_code
from Detectors.complex_method import detect_complex_method
from Detectors.complex_lambda_function import detect_complex_lambda



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
    complexity=3 # complexity=num of child+ binary/boolean operators in a lambda

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
def process_data(data, threshold):
    filtered_data = filter(lambda x: x["value"] > threshold and (x["name"] == "foo" or x["priority"] > 10), data)
    funcs = [lambda x: x + i for i in range(3)]
    sorted_data = sorted(filtered_data, key=lambda x: ((x["value"] * 2) + (x["priority"] / 3)) * (1 if x["active"] else -1))
    return sorted_data

result = process_data(data, 10)

"""

print(detect_code_smells(input_code))

