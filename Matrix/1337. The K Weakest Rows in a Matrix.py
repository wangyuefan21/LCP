# You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians).
# The soldiers are positioned in front of the civilians.
# That is, all the 1's will appear to the left of all the 0's in each row.
#
# A row i is weaker than a row j if one of the following is true:
# 1. The number of soldiers in row i is less than the number of soldiers in row j.
# 2. Both rows have the same number of soldiers and i < j.
# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

# vertical scan to find 0s and add row number to visited and ans if it is not in visited yet
# add from more if the ans has not reached to k yet
def kWeakestRows(mat, k):
    """
    :type mat: List[List[int]]
    :type k: int
    :rtype: List[int]
    """
    m = len(mat)
    n = len(mat[0])
    visit = set()
    ans = []
    # find 0s in matrix and add row number to ans, make sure they are not duplicated
    for j in range(n):
        for i in range(m):
            if mat[i][j] == 0:
                if i not in visit:
                    visit.add(i)
                    ans.append(i)
                    if len(ans) == k:
                        return ans
    # add more make ans reach to k elements
    i = 0
    while True:
        if len(ans) == k:
            return ans
        if i not in visit:
            visit.add(i)
            ans.append(i)
        i += 1

if __name__ == '__main__':
    mat = [[1, 1, 0, 0, 0],
           [1, 1, 1, 1, 0],
           [1, 0, 0, 0, 0],
           [1, 1, 0, 0, 0],
           [1, 1, 1, 1, 1]]
    k = 3
    assert kWeakestRows(mat, k) == [2,0,3]

    mat = [[1,1,1,1,1,1],
           [1,1,1,1,1,1],
           [1,1,1,1,1,1]]
    k = 2
    assert kWeakestRows(mat, k) == [0,1]

    mat = [[1,1,1,1,1,0],
           [1,1,1,1,1,1],
           [1,1,1,1,1,1]]
    k = 3
    assert kWeakestRows(mat, k) == [0,1,2]