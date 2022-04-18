import ast
import json
from collections import defaultdict

class AstGraphGenerator(ast.NodeVisitor):
    
    def __init__(self, source):
        self.graph = defaultdict(lambda: [])
        self.source = source

    def __str__(self):
        return str(self.graph)
    
    def get_graph(self):
        return dict(self.graph)
    
    def _getid(self, node):
        try:
            lineno = node.lineno - 1
            return "%s: %s" % (type(node), '')

        except AttributeError:
            return type(node)

    def visit(self, node):
        """Visit a node."""
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        """Called if no explicit visitor function exists for a node."""
        for _, value in ast.iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, ast.AST):
                        self.visit(item)

            elif isinstance(value, ast.AST):
                node_source = self._getid(node)
                value_source = self._getid(value)
                self.graph[node_source].append(value_source)
                self.visit(value)
                
if __name__ == '__main__':
    with open("examples/addition.py", "r") as source:
        node = ast.parse(source.read())
        tree = ast.dump(node)
        
        # graph_generator = AstGraphGenerator(source.readlines())
        # graph_generator.visit(node)
        # print(graph_generator)

    tree = {}
    for node in ast.walk(ast.parse("""print('Hello, World!')""")):
        for field_name, child_node in ast.iter_fields(node):
            if child_node is not None and child_node != []:
                tree[node.__class__.__name__] = tree.get(node.__class__.__name__, (field_name, child_node))
                # print(field_name, child_node)
                
    print(tree)