# A binary string is monotone increasing if it consists of some number of 0's (possibly none),
# followed by some number of 1's (also possibly none).
# You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.
# Return the minimum number of flips to make s monotone increasing.

# 1 ignore all 0s until find the first 1
# 2.1 keep as 1 and the substring has to be all 1s; ,
# 2.2 flip to 0 repeat the processes on the substrings
# 3 stop when reaching to the end of the string
# find how many '0's after given index to make 2.1 O(1)
def minFlipsMonoIncr(s):
    """
    :type s: str
    :rtype: int
    """
    # find how many '0's after a given index
    dp = [0 for _ in range(len(s))]
    zeros = 0
    for i in range(len(s) - 1, -1, -1):
        dp[i] = zeros
        if s[i] == '0':
            zeros += 1
    # helper function to bran the string
    def branch(s, i, count):
        if i > len(s) - 1:
            return count
        while i < len(s) and s[i] == '0':
            i += 1
        if i > len(s) - 1:
            return count
        not_flip = count + dp[i]
        flip = branch(s, i + 1, count + 1)
        return min(not_flip, flip)

    return branch(s, i, 0)

if __name__ == '__main__':
    s = "00110"
    assert minFlipsMonoIncr(s) == 1
    s = "010110"
    assert minFlipsMonoIncr(s) == 2
    s = "00011000"
    assert minFlipsMonoIncr(s) == 2