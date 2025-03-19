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
 