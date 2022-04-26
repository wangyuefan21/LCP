# Given the root of a binary tree, return the level order traversal of its nodes' values.
# (i.e., from left to right, level by level).

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS
# pop nodes and add nodes from the subtree level by level from left to right
def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if root is None:
        return []
    ans = []
    queue = [root]
    while queue:
        temp_ans = []
        num2pop = len(queue)
        for _ in range(num2pop):
            cur = queue.pop(0)
            temp_ans.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        ans.append(temp_ans)
    return ans

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(levelOrder(root))
    assert levelOrder(root) == [[3],[9,20],[15,7]]
