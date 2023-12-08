def detect_long_method(node, code):
    threshold = 20  # You can adjust this value based on your preference.
    direct_children_count = len(node.children)

    if direct_children_count > threshold:
        return [node]  # Return the method node itself as a code smell.
    else:
        return []
