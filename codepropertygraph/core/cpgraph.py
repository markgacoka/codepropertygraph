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
        files_list = []
        files_count = 0
        directory_count = 0
        for base, dirs, files in os.walk(input_path):
            for directory in dirs:
                directory_count += 1
            for single_file in files:
                files_count += 1
                files_list.append(single_file)
        return files_list, (directory_count, files_count)
