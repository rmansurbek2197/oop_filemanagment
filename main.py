class File:
    def __init__(self, fid, name, size):
        self.fid = fid
        self.name = name
        self.size = size


class FileSystem:
    def __init__(self):
        self.files = {}

    def upload(self, file):
        self.files[file.fid] = file

    def delete(self, fid):
        if fid in self.files:
            del self.files[fid]

    def total_size(self):
        return sum(f.size for f in self.files.values())

    def largest_file(self):
        return max(self.files.values(), key=lambda f: f.size)
