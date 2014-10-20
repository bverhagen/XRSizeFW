import os

class File:
    def __init__(self, path):
        self.path = path
        self.filename = os.path.basename(path)

    def getFilename(self):
        return self.filename

    def getPath(self):
        return self.path

    def isDir(self):
        return os.path.isdir(self.path)

    def getSubDirs(self):
        if not self.isDir():
            return None
        subDirs = [os.path.join(self.path,o) for o in os.listdir(self.path) if os.path.isdir(os.path.join(self.path,o))]
        subDirList = []
        for singleDir in subDirs:
            subDirList.append(File(singleDir))

        return subDirList

