# Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.
# In one shift operation:
# Element at grid[i][j] moves to grid[i][j + 1].
# Element at grid[i][n - 1] moves to grid[i + 1][0].
# Element at grid[m - 1][n - 1] moves to grid[0][0].
# Return the 2D grid after applying shift operation k times.

# flat the matrix to an array
# move the last k%(m*n) items to the beginning following by the rest
# construct shifted matrix by the array

def shiftGrid(grid, k):
    """
    :type grid: List[List[int]]
    :type k: int
    :rtype: List[List[int]]
    """
    m = len(grid)
    n = len(grid[0])
    k = k % (m * n)
    flat = [item for sublist in grid for item in sublist]
    flat = flat[-k:] + flat[:-k]
    ans = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            ans[i][j] = flat[n * i + j]
    return ans

if __name__ == "__main__":
    grid = [[1],[2],[3],[4],[7],[6],[5]]
    k = 23
    assert shiftGrid(grid, k) == [[6],[5],[1],[2],[3],[4],[7]]

    grid = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
    k = 4
    assert shiftGrid(grid, k) == [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]