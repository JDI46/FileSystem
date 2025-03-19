from tree import Tree as t
from linked_list import LinkedList as lst

   

class FileSystem:
    def mkdir(t, file_name):
        #makes a new file in the tree
        if t.label == file_name:
            raise Exception("File Exists")
        else:
            new_file = t.label + str(file_name)
            return str(new_file)


    def rm(t, lst):
        #go into the tree and delete a file
        pass
    def touch(lst):
        #makes a node within the tree
        pass

    def ls(t):
        #lists the tree label
        pass

    def cd(t):
        #goes into the tree and retains state
        pass

    def cp(t, lst):
        #copies the the tree and contents and dupicates
        pass

    def mv(t, lst):
        pass

    def find(t, lst):
        pass




