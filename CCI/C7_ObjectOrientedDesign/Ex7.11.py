class FileSystem():
    def __init__(self):
        self.dir = []

    def create_file(self, name):
        file = File(name)
        self.dir.append(file)

    def search(self, name):
        # Trie or Linear Search
        pass

    def delete(self, name):
        file = self.search(name)
        self.dir.remove(file)
        
    def create_directory(self, dir):
        dir = Directory()
        self.dir.append(dir)

class Directory():
    def __init__(self, name):
        self.name = name
        self.files = []

    def rename(self, name):
        self.name = name

class File():
    def __init__(self, name):
        self.name = name
        self.content = []

    def rename(self, name):
        self.name = name

    def modify(self, contents):
        self.contents = contents
