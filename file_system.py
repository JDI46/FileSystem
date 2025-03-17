import asyncio, threading

class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches
    
    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return f'Tree({self.label}{self.branches})'

    def  __str__(self):

        def indented(self):
            lines = []
            for b in self.branches:
                for line in indented(b):
                    lines.append(' ' + line)
            return [str(self.label)] + lines
    
        return '\n'.join(indented(self))
    

class Node:
    #node will be a document or thing in the file
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class FileSystem:
    def mkdir(self):
        #makes a new file in the tree
        pass

    def rm(self):
        pass

    def touch(self):
        #makes a node within the tree
        pass

    def ls(self):
        #lists the tree label
        pass

    def cd(self):
        #goes into the tree and retains state
        pass

    def cp(self):
        #copies the the tree and contents and dupicates
        pass

    def mv(self):
        pass

    def find(self):
        pass

    def cat(self):
        pass




