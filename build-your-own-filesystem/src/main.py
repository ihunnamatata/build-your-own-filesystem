"""
Build Your Own Filesystem – In-Memory File/Folder Structure
Author: Ihunna Amugo | Build-Your-Own-X Series

📁 Goal:
Build a fake in-memory filesystem shell that supports:
- mkdir, touch, write, read, ls, cd, pwd, exit

🩺 Real-World Parallel:
Simulates how imaging files, patient simulations, or model logs are structured inside EHR or PACS systems.

This is a model for internal simulation file tracking, cloud staging, or digital twin folders.
"""

class Node:
    def __init__(self, name, is_folder=False):
        self.name = name
        self.is_folder = is_folder
        self.children = {}  # For folders
        self.content = ""   # For files

class FileSystem:
    def __init__(self):
        self.root = Node("/", is_folder=True)
        self.cwd = self.root
        self.path = [self.root]

    def pwd(self):
        return "/" + "/".join([node.name for node in self.path if node.name != "/"])

    def mkdir(self, name):
        if name in self.cwd.children:
            print("Folder already exists.")
            return
        self.cwd.children[name] = Node(name, is_folder=True)

    def touch(self, name):
        if name in self.cwd.children:
            print("File already exists.")
            return
        self.cwd.children[name] = Node(name, is_folder=False)

    def ls(self):
        for name in self.cwd.children:
            node = self.cwd.children[name]
            marker = "/" if node.is_folder else ""
            print(name + marker)

    def cd(self, name):
        if name == "..":
            if len(self.path) > 1:
                self.path.pop()
                self.cwd = self.path[-1]
        elif name in self.cwd.children and self.cwd.children[name].is_folder:
            self.cwd = self.cwd.children[name]
            self.path.append(self.cwd)
        else:
            print("Folder not found.")

    def write(self, name, text):
        if name not in self.cwd.children:
            print("File not found.")
            return
        node = self.cwd.children[name]
        if node.is_folder:
            print("Cannot write to a folder.")
            return
        node.content = text

    def read(self, name):
        if name not in self.cwd.children:
            print("File not found.")
            return
        node = self.cwd.children[name]
        if node.is_folder:
            print("Cannot read a folder.")
            return
        print(node.content)

def shell():
    fs = FileSystem()
    print("🗂️ Ihunna's Simulated Filesystem. Type 'exit' to quit.")
    while True:
        cmd = input(f"{fs.pwd()}$ ").strip()
        if cmd == "exit":
            break
        elif cmd.startswith("mkdir "):
            fs.mkdir(cmd.split(" ", 1)[1])
        elif cmd.startswith("touch "):
            fs.touch(cmd.split(" ", 1)[1])
        elif cmd.startswith("cd "):
            fs.cd(cmd.split(" ", 1)[1])
        elif cmd == "ls":
            fs.ls()
        elif cmd == "pwd":
            print(fs.pwd())
        elif cmd.startswith("write "):
            parts = cmd.split(" ", 2)
            if len(parts) == 3:
                fs.write(parts[1], parts[2].strip('"'))
            else:
                print("Usage: write <file> "<text>"")
        elif cmd.startswith("read "):
            fs.read(cmd.split(" ", 1)[1])
        else:
            print("Unknown command.")

if __name__ == "__main__":
    shell()
