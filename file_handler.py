import os
import shutil


class File_handler:
    def __init__(self, dir):
        self.dir = dir  # Making it possible to choose a directory'.

    def join(self, file):
        return os.path.join(self.dir, file)  # Adds up the directory and choosen file.

    def ls(self):
        ls = os.listdir(self.dir)  # Listing all files in direciry
        ls.sort()
        return ls

    def size(self, file):
        resp = os.stat(self.join(file))  # Returning the size of a file
        return resp.st_size

    def rm(self, file):
        os.remove(self.join(file))  # Removes a file
        return "File removed"

    def cp(self, file1, file2):  # Copying 2 mock files to make the list complete after removing a file.
        shutil.copy(file1, file2)
        return "File copied"
