import ast

class ASTTraversal(ast.NodeVisitor):
    
    # def generic_visit(self, node):
    #     print(type(node).__name__)
    #     self.generic_visit(node)
        
    def visit_Module(self, node):
        self.names = set()
        print('Node type: Module\nFields: ', node._fields)
        self.generic_visit(node)
        
    def visit_Expr(self, node):
        print('Node type: Expr\nFields: ', node._fields)
        self.generic_visit(node)

    def visit_Call(self, node):
        print('Node type: Call\nFields: ', node._fields)
        self.generic_visit(node)

    def visit_Name(self, node):
        print('Node type: Name\nFields: ', node._fields)
        self.generic_visit(node)
        
    def visit_Load(self, node):
        self.generic_visit(node)
        
    def visit_Constant(self, node):
        print('Node type: Constant\nFields: ', node._fields)
        self.generic_visit(node)
        
        
if __name__ == '__main__':
    # with open("examples/addition.py", "r") as source:
    #     node = ast.parse(source.read())
    #     tree = ast.dump(node)

    # tree = astor.code_to_ast.parse_file("examples/addition.py")
    node = ast.parse("print('hello world')")
    tree = ast.dump(node, indent=2)
    print(tree)
    abstract_syntax_tree = ASTTraversal()
    abstract_syntax_tree.visit(node)