# Given the root of a binary tree, return the level order traversal of its nodes' values.
# (i.e., from left to right, level by level).

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if root is None:
        return []
    ans = []
    quene = [root]
    while quene:
        temp_ans = []
        num2pop = len(quene)
        for _ in range(num2pop):
            cur = quene.pop(0)
            temp_ans.append(cur.val)
            if cur.left:
                quene.append(cur.left)
            if cur.right:
                quene.append(cur.right)
        ans.append(temp_ans)
    return ans

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(20)
    root.right.right = TreeNode(20)
    print(levelOrder(root))
    assert levelOrder(root) == [[3], [9, 20], [20, 20]]