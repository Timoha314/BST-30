class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self):
        self.root = None

def insert(x):
    parent = None
    v = tree.root
    while v is not None:
        parent = v
        if x < v.key:
            v = v.left
        elif x > v.key:
            v = v.right
        else:
            return
    w = Node(x)
    if parent is None:
        tree.root = w
    elif x < parent.key:
        parent.left = w
    else:
        parent.right = w

def height(node):
    if node is None:
        return -1
    else:
        return max(height(node.left), height(node.right)) + 1

def find_node(root,result):
    if root is None:
        return None
    left_height = height(root.left)
    right_height = height(root.right)
    if abs(left_height - right_height) == 2:
        result.append(root)
    find_node(root.left, result)
    find_node(root.right, result)

def replace_child(parent, old, new):
    if parent is None:
        tree.root = new
    elif parent.left == old:
        parent.left = new
    elif parent.right == old:
        parent.right = new

def delete(x):
    parent = None
    v = tree.root
    while True:
        if v is None:
            return
        if x < v.key:
            parent = v
            v = v.left
        elif x > v.key:
            parent = v
            v = v.right
        else:
            break
    result = None
    if v.left is None:
        result = v.right
    elif v.right is None:
        result = v.left
    else:
        min_node_parent = v
        min_node = v.left
        while min_node.right is not None:
            min_node_parent = min_node
            min_node = min_node.right
        v.key = min_node.key
        replace_child(min_node_parent, min_node, min_node.left)
        return
    replace_child(parent, v, result)

def PreOrderTraversalLeft(v, result):
    if v is None:
        return
    stack = [v]
    while stack:
        node = stack.pop()
        result.append(str(node.key))
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

with open('input.txt', 'r') as file:
    lines = file.readlines()
tree = Tree()
root_value = int(lines[0].strip())
tree.root = Node(root_value)
for line in lines[1:]:
    line = line.strip()
    if line:
        n = int(line)
        insert(n)
Arr = []
find_node(tree.root, Arr)
Res = []
for i in range(len(Arr)):
    Res.append(Arr[i].key)
if Res:
    Res.sort()
    if len(Arr) % 2 == 1:
        delete (Res[len(Arr) // 2])
result = []
PreOrderTraversalLeft(tree.root, result)
with open('output.txt', 'w') as output_file:
    output_file.write('\n'.join(result) + '\n')
