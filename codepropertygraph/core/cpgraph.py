class CPG:
    def __init__(self, input_path):
        self.input_path = input_path
        self.graph = {}
    
    def __repr__(self):
        return 'Graph: {}'.format(self.graph)