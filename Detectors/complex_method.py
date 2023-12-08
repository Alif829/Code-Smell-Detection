def detect_complex_method(node, max_nesting_level, max_statement_count):
    
    # Detect complex method based on nesting level and statement counts within the method

    complex_nodes = []
    current_statement_count = 0

    def traverse(node, depth=0):
        nonlocal current_statement_count
        if node.type in ['if_statement', 'for_statement', 'while_statement']:
            current_statement_count += 1 
            if depth > max_nesting_level or current_statement_count > max_statement_count:
                complex_nodes.append(node)
                return 

            for child in node.children:
                traverse(child, depth + 1)  # Recursively traverse all the children
        else:
            for child in node.children:
                traverse(child, depth)

    traverse(node)
    return complex_nodes
