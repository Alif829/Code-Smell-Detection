def detect_complex_lambda(node, complexity):
   
    # A lambda is complex if it exceeds
    #         num of child nodes
    #         num of nested expressions
    #         num of operator count

    complex_lambdas = []

    # Function to calculate complexity of a node based on number of children and operators
    def calculate_complexity(node):
        complexity = 0
        if node.type == "binary_operator" or node.type == "boolean_operator":
            complexity += 1
        complexity += len(node.children)
        return complexity

    # Recursive function to traverse the AST
    def traverse(node):
        if node.type == "lambda":
            lambda_complexity = calculate_complexity(node)
            if lambda_complexity > complexity:      # complexity= num of child+ binary/boolean operators
                complex_lambdas.append(node)
            return

        for child in node.children:
            traverse(child)

    traverse(node)
    return complex_lambdas

