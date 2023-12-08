def detect_long_method(node, code, child_threshold):

    # If number of children of a method exceeds the threshold it is large method
    
    direct_children_count = len(node.children)

    if direct_children_count > child_threshold:
        return [node]  # Return the method node itself as a code smell.
    else:
        return []
