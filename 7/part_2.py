import os
import json


def main():
    with open(os.path.join(os.path.dirname(__file__), "./input.txt"), 'r') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]
    tree = {}
    current_directory = []
    for line in lines:
        if line.startswith('$ '):
            if line[2:].startswith('cd'):
                _, param = line[2:].split(' ', 1)
                if param == '..':
                    current_directory = current_directory[:-1]
                elif param == '/':
                    current_directory = []
                else:
                    current_directory.append(param)
            # elif cmd == 'ls':
        else:
            size, name = line.split(' ', 1)
            path_ref = tree
            for cd in current_directory:
                if cd not in path_ref.keys():
                    path_ref[cd] = {'*type': 'dir'}
                path_ref = path_ref[cd]
            if size == 'dir':
                if name not in path_ref.keys():
                    path_ref[name] = {'*type': 'dir'}
            else:
                size = int(size)
                path_ref[name] = {'*type': 'file', '*size': size}

    def count_size(tree):
        size_sum = 0
        for obj in tree.values():
            if type(obj) == type(''):
                continue
            if obj['*type'] == 'file':
                size_sum += obj['*size']
            else:
                size_sum += count_size(obj)
        return size_sum

    def list_sizes(tree):
        sizes = []
        for obj in tree.values():
            if type(obj) == type(''):
                continue
            if obj['*type'] == 'dir':
                sizes.append(count_size(obj))
                sizes += list_sizes(obj)
        return sizes

    sizes = list_sizes(tree)
    whole_size = count_size(tree)
    for size in sorted(sizes):
        if 70000000 - whole_size + size >= 30000000:
            return size


if __name__ == "__main__":
    print(main())
