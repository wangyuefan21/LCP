# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Divide and Conquer
# Divide: ontinue to divide strs into left and right subarray until there are only one or two strings in the array
# Conquer: find the longest prefix of the left and right subarray.

def longestCommonPrefix(strs):
    def find_prefix(left, right):
        prefix = ''
        for i in range(min(len(left), len(right))):
            if left[i] != right[i]:
                break
            prefix += left[i]
        return prefix
    def split(strs, l, r):
        if l == r:
            return strs[l]
        if l == r-1:
            return find_prefix(strs[l], strs[r])
        else:
            left = split(strs, l, (l+r)//2)
            right = split(strs, (l+r)//2+1, r)
            return find_prefix(left, right)
    return split(strs, 0, len(strs)-1)

# Vertical Scan
# Compare letter by letter of the first word in the strs to the rest
# Break until the letter do not match or the word is too long

def longestCommonPrefix_vertical_scan(strs):
    prefix = ''
    for i in range(len(strs[0])):
        check = strs[0][i]
        for j in range(1, len(strs)):
            if i > len(strs[j])-1 or strs[j][i] != check:
                return prefix
        prefix += check
    return prefix

