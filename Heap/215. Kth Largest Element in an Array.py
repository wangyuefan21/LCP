# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Maintain a heap with length k
def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    h = []
    for num in nums:
        heapq.heappush(h, num)
        if len(h) > k:
            heapq.heappop(h)
    return h[0]

def quick_select(nums, k):
    pivot = nums[-1]
    left = [x for x in nums if x > pivot]
    mid = [x for x in nums if x == pivot]
    right = [x for x in nums if x < pivot]

    if k <= len(left):
        return quick_select(left, k)
    elif k > len(left) + len(mid):
        return quick_select(right, k-len(left)-len(mid))
    else:
        return mid[0]

if __name__ == '__main__':
    import heapq
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(findKthLargest(nums, k))
    print(quick_select(nums, k))
    assert findKthLargest(nums, k) == 5
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(findKthLargest(nums, k))
    print(quick_select(nums, k))
    assert findKthLargest(nums, k) == 4
