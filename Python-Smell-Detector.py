import tree_sitter
from Detectors.long_parameter_list import detect_long_parameter_list
from Detectors.large_method import detect_long_method
from Detectors.excessive_returns import detect_excessive_returns
from Detectors.code_duplication import detect_duplicate_code
from Detectors.complex_method import detect_complex_method
from Detectors.compex_lambda import detect_complex_lambda


def generate_ast(code):
    PYTHON_LANGUAGE = tree_sitter.Language('E:/tree-sitter-python/tree-sitter-python.dll', 'python')
    parser = tree_sitter.Parser()
    parser.set_language(PYTHON_LANGUAGE)
    tree = parser.parse(bytes(code, "utf8"))
    return tree

def detect_code_smells(code):
    tree = generate_ast(code)
    root_node = tree.root_node

    smells = []

    for node in root_node.children:
        node_code = code[node.start_byte:node.end_byte]

        if node.type == 'function_definition':
            # # Duplicated Code Smell
            # duplicate_code_issues = detect_duplicate_code(node, code)
            # for issue in duplicate_code_issues:
            #     smells.append((issue, 'Duplicate Code'))
            
            # # Long Parameter List Smell
            # if detect_long_parameter_list(node):
            #     smells.extend([(smell_node, 'Long Parameter List') for smell_node in detect_long_parameter_list(node)])
            
            # # Excessive Return Smell
            # excessive_returns = detect_excessive_returns(node)
            # if excessive_returns:
            #     for return_node in excessive_returns:
            #         smells.append((return_node, 'Excessive Returns'))

            # Complex Method Smell
            complex_method_issues = detect_complex_method(node)
            for issue in complex_method_issues:
                smells.append((issue, 'Complex Method'))
            
            # Complex Lambda Smell
            complex_lambdas = detect_complex_lambda(node,1)
            for issue in complex_lambdas:
                smells.append(issue)

            # large_method_issues = detect_long_method(node,code)
            # for issue in large_method_issues:
            #     smells.append((issue, 'Large Method'))

    return smells


# Example usage
code_sample = """
def calculate_and_return_result(a, b):
    result = a + b
    # Complex Lambda (nested and long)
    filtered_data = filter(lambda x: x["value"] > 10 and x["name"] in ["foo", "bar"], data)
    # Another complex lambda (high depth)
    sorted_data = sorted(data, key=lambda x: (x["value"] * 2) + (x["priority"] / 3))
    return result
"""

print(detect_code_smells(code_sample))
