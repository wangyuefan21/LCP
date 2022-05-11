# Given an integer n, return the number of strings of length n that consist
# only of vowels (a, e, i, o, u) and are lexicographically sorted.
# A string s is lexicographically sorted if for all valid i,
# s[i] is the same as or comes before s[i+1] in the alphabet.

# non-DP version
def countVowelStrings(n: int) -> int:
    if n == 1:
        return 5
    if n == 2:
        return 15
    cur = [5, 4, 3, 2, 1]
    for _ in range(n - 2):
        temp = []
        for num in cur:
            if num == 5:
                temp += [5, 4, 3, 2, 1]
            elif num == 4:
                temp += [4, 3, 2, 1]
            elif num == 3:
                temp += [3, 2, 1]
            elif num == 2:
                temp += [2, 1]
            elif num == 1:
                temp += [1]
        cur = temp
    return sum(cur)

if __name__ == '__main__':
    n = 1
    assert countVowelStrings(n) == 5
    n = 2
    assert countVowelStrings(n) == 15
    n = 33
    assert countVowelStrings(n) == 66045
    print(countVowelStrings(n))