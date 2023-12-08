

def gather_expression_statements(node):
    
    # Recursively gather all expression_statement nodes from the given node.
    
    nodes = []
    if node.type == 'expression_statement':
        nodes.append(node)
    
    for child in node.children:
        nodes.extend(gather_expression_statements(child))
    
    return nodes

def detect_duplicate_code(node, code):
    
    # Detect duplicate expression statements within the given node's AST.
    # Args:
    #   node: The root node of the AST to check
    #   code(str): The source code corresponding to the AST.
    # Returns nodes with duplicate codes

    def get_descendants_with_type(node, node_type):
        
        # Gather all nodes of a specific type
        descendants = []
        if node.type == node_type:
            descendants.append(node)
        
        for child in node.children:
            descendants.extend(get_descendants_with_type(child, node_type))
            
        return descendants

    # Gathering all 'expression_statement' nodes from the AST
    all_expression_statements = get_descendants_with_type(node, 'expression_statement')

    # Mapping code snippets to their respective AST nodes
    code_snippets = {}
    
    for expr_node in all_expression_statements:
        snippet = code[expr_node.start_byte:expr_node.end_byte].strip()
        if snippet not in code_snippets:
            code_snippets[snippet] = [expr_node]
        else:
            code_snippets[snippet].append(expr_node)

    # Extracting nodes with duplicate code snippets
    duplicate_nodes = [nodes for snippet, nodes in code_snippets.items() if len(nodes) > 1]
    
    # Preparing the result: a list of nodes with their associated 'Duplicate Code' label
    duplicates = [(node, 'Duplicate Code') for nodes in duplicate_nodes for node in nodes]
    
    return duplicates
