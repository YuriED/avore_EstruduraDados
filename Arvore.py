class Node:
    def _init_(self, key):
        self.left = None
        self.right = None
        self.value = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key <= root.value:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def preorder(root):
    if root:
        print(root.value, end=' ')
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=' ')
        inorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=' ')


def levelorder(root):
    if not root:
        return

    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.value, end=' ')

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


tree = None

for _ in range(20):
    num = random.randint(0, 100)
    tree = insert(tree, num)


print("Árvore antes da remoção:")
print("Pré-ordem:", end=' ')
preorder(tree)
print("\nIn-ordem:", end=' ')
inorder(tree)
print("\nPós-ordem:", end=' ')
postorder(tree)
print("\nEm nível:", end=' ')
levelorder(tree)


for _ in range(5):
    num = random.randint(0, 100)
    tree = insert(tree, num)


print("\n\nÁrvore após a remoção:")
print("Pré-ordem:", end=' ')
preorder(tree)
print("\nIn-ordem:", end=' ')
inorder(tree)
print("\nPós-ordem:", end=' ')
postorder(tree)
print("\nEm nível:", end=' ')
levelorder(tree)