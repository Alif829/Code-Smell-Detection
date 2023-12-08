
def detect_excessive_returns(node):
    return_nodes = find_return_statements(node)
    if len(return_nodes) > 2:
        return return_nodes[2:]  # Return only the excess nodes
    return []

def find_return_statements(node):
    returns = []
    if node.type == 'return_statement':
        returns.append(node)
    for child in node.children:
        returns.extend(find_return_statements(child))
    return returns
