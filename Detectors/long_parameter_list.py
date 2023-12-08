def detect_long_parameter_list(node):
    parameters = [child for child in node.children if child.type == 'parameters']
    if not parameters:
        return []

    actual_parameters = [param for param in parameters[0].children if param.type == 'identifier']
    
    if len(actual_parameters) > 3:  # Threshold
        return actual_parameters
    
    return []
