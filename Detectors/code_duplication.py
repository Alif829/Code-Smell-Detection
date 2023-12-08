def node_identifier(node):
    """
    Create a unique identifier string for the node based on its type, start_byte, and end_byte.
    
    Args:
    - node (tree_sitter.Node): The node for which to generate an identifier.

    Returns:
    - str: Unique identifier for the node.
    """
    return f"{node.type}_{node.start_byte}_{node.end_byte}"

def gather_expression_statements(node):
    """
    Recursively gather all expression_statement nodes from the given node.
    
    Args:
    - node (tree_sitter.Node): The root node from which to gather expression_statement nodes.

    Returns:
    - list: List of all expression_statement nodes within the tree rooted at the given node.
    """
    nodes = []
    if node.type == 'expression_statement':
        nodes.append(node)
    
    for child in node.children:
        nodes.extend(gather_expression_statements(child))
    
    return nodes

def detect_duplicate_code(node, code):
    """
    Detect duplicate expression statements within the given node's AST.

    Args:
    - node (tree_sitter.Node): The root node of the AST to check.
    - code (str): The source code corresponding to the AST.

    Returns:
    - list: List of tuples where each tuple contains a duplicate node and its associated label.
    """
    def get_descendants_with_type(node, node_type):
        """
        Recursively gather all nodes of a specific type from the given node.
        
        Args:
        - node (tree_sitter.Node): The root node from which to gather specific type nodes.
        - node_type (str): The desired type of nodes to gather.

        Returns:
        - list: List of all nodes of the specified type within the tree rooted at the given node.
        """
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
