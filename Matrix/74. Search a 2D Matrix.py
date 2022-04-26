# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.
#
# This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

# treat the matrix as array
# matrix[index/m][index%m]
def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    left = 0
    right = m*n-1
    while left <= right:
        mid = (left+right)//2
        check = matrix[mid//m][mid%m]
        if check == target:
            return True
        elif check < target:
            left = mid + 1
        else:
            right = mid -1
    return False

if __name__ == '__main__':
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    assert searchMatrix(matrix, target) == True
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    assert searchMatrix(matrix, target) == False