def detect_long_parameter_list(node):
    
    ##
    # In the function_definition node there are 3 children: identifier, parameters and body
    # Parameter children are identifiers. They are the actual children
    # # 

    ## Long parameter smell if parameters count>5 (usually)

    parameters = [child for child in node.children if child.type == 'parameters']
    if not parameters:
        return []

    actual_parameters = [param for param in parameters[0].children if param.type == 'identifier']
    
    if len(actual_parameters) > 3:  # Threshold
        return actual_parameters
    
    return []
