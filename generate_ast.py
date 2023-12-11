import tree_sitter

def generate_ast(code):
    PYTHON_LANGUAGE = tree_sitter.Language('E:/tree-sitter-python/tree-sitter-python.dll', 'python')
    parser = tree_sitter.Parser()
    parser.set_language(PYTHON_LANGUAGE)
    tree = parser.parse(bytes(code, "utf8"))
    return tree