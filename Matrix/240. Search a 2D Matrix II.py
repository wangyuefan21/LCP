# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.

# This matrix has the following properties:
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

# search from top right corner
def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    m = len(matrix)
    n = len(matrix[0])
    i = 0
    j = n - 1
    while i < m and j > -1:
        num = matrix[i][j]
        if num == target:
            return True
        elif num > target:
            j -= 1
        else:
            i += 1
    return False

if __name__ == '__main__':
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    assert searchMatrix(matrix, target) == True
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 20
    assert searchMatrix(matrix, target) == False
