import os
import sys
sys.dont_write_bytecode = True

class CPG:
    def __init__(self, input_path):
        self.input_path = input_path
        self.graph = {}
        self.files = WorkSpaceFiles(input_path)
    
    def __repr__(self):
        return 'Graph: {}'.format(self.graph)

class WorkSpaceFiles:
    def __init__(self, input_path):
        self.l, self.count = self.file_count(input_path)
        self.input_path = input_path

    def file_count(self, input_path):
        files_num = 0
        files_list = []
        for _, _, files in os.walk(r'{}'.format(input_path)):
            files_num = sum(len(files))
            files_list.append(files)
        return files_list, files_num
