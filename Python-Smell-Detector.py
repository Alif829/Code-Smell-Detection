import tree_sitter
from Detectors.long_parameter_list import detect_long_parameter_list
from Detectors.large_method import detect_long_method
from Detectors.excessive_returns import detect_excessive_returns
from Detectors.high_cyclomatic_complexity import detect_high_cyclomatic_complexity
from Detectors.inconsistent_naming import detect_inconsistent_naming
from Detectors.code_duplication import detect_duplicate_code



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
            if detect_long_parameter_list(node):
                smells.extend([(smell_node, 'Long Parameter List') for smell_node in detect_long_parameter_list(node)])
            
            large_method_issues = detect_long_method(node,code)
            for issue in large_method_issues:
                smells.append((issue, 'Large Method'))
            
            if detect_high_cyclomatic_complexity(code):
                smells.append((node, 'High Cyclomatic Complexity'))
            
            inconsistent_names = detect_inconsistent_naming(node, node_code)
            for naming_node in inconsistent_names:
                smells.append((naming_node, 'Inconsistent Naming'))

            excessive_returns = detect_excessive_returns(node)
            if excessive_returns:
                for return_node in excessive_returns:
                    smells.append((return_node, 'Excessive Returns'))
            
            duplicate_code_issues = detect_duplicate_code(node, code)
            for issue in duplicate_code_issues:
                smells.append((issue, 'Duplicate Code'))


    return smells


# Example usage
code_sample = """
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

print(detect_code_smells(code_sample))
