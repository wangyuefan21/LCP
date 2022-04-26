# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
# (i.e., from left to right, then right to left for the next level and alternate between).

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS use to flag to represent if the queue left from level nodes or right nodes
# ans is structure directly from queue
# next queue need to be queue up differently depends on the start of the current queue
# reverse the queue every iteration
def zigzagLevelOrder_initial(root):
    if root is None:
        return []
    ans = []
    queue = [root]
    flag = 1
    while queue:
        temp_ans = []
        num2pop = len(queue)
        for _ in range(num2pop):
            cur = queue.pop(0)
            temp_ans.append(cur.val)
            if flag == 1:
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            elif flag == -1:
                if cur.right:
                    queue.append(cur.right)
                if cur.left:
                    queue.append(cur.left)
        ans.append(temp_ans)
        queue = queue[::-1]
        flag *= -1
    return ans

def zigzagLevelOrder(root):
    if root is None:
        return []
    ans = []
    queue = [root]
    flag = 1
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
        if flag == 1:
            ans.append(temp_ans)
        else:
            ans.append(temp_ans[::-1])
        flag *= -1
    return ans

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(zigzagLevelOrder(root))
    assert zigzagLevelOrder(root) == [[3],[20,9],[15,7]]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print(zigzagLevelOrder(root))
    assert zigzagLevelOrder(root) == [[1], [3, 2], [4, 5]]