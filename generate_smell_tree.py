import tree_sitter
from graphviz import Digraph

def traverse_and_create_graph(node, graph, highlighted_nodes, parent=None):
    """
    Recursively traverse the AST and add nodes and edges to the Graphviz graph.
    Nodes in the highlighted_nodes list will be colored red.
    """
    # Determine the color of the node
    color = "red" if node.type in highlighted_nodes else "black"

    # Add the current node to the graph with the specified color
    current_node_name = f"{node.type}_{node.id}"
    graph.node(current_node_name, label=node.type, color=color, fontcolor=color)

    # If there is a parent, add an edge from parent to current node
    if parent:
        graph.edge(parent, current_node_name)

    # Traverse children of the current node
    if node.children:
        for child in node.children:
            traverse_and_create_graph(child, graph, highlighted_nodes, current_node_name)

def generate_ast_graph(source_code, language, highlighted_nodes):
    """
    Generate an AST from the source code and create a graphical representation.
    Nodes in the highlighted_nodes list will be colored red.
    """
    # Load the language parser
    parser = tree_sitter.Parser()
    parser.set_language(language)

    # Parse the source code to generate the AST
    tree = parser.parse(bytes(source_code, "utf8"))
    root_node = tree.root_node

    # Create a Graphviz graph
    graph = Digraph(comment='AST', format='png')

    # Recursively traverse the AST and add to the graph
    traverse_and_create_graph(root_node, graph, highlighted_nodes)

    return graph

