# Given an integer n, return the number of strings of length n that consist
# only of vowels (a, e, i, o, u) and are lexicographically sorted.
# A string s is lexicographically sorted if for all valid i,
# s[i] is the same as or comes before s[i+1] in the alphabet.

# non-DP version
# expand list level by level into final count
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

def countVowelStrings_dp(n: int) -> int:
    dp = {(2,'a'):5, (2,'e'):4, (2,'i'):3, (2,'o'):2, (2,'u'):1}
    def count(n, last_char):
        if n == 1:
            return 1
        if (n, last_char) in dp:
            return dp[(n, last_char)]
        ans = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        for vowel in vowels:
            if vowel >= last_char:
                ans += count(n-1, vowel)
        dp[(n, last_char)] = ans
        return dp[(n, last_char)]
    vowels = ['a', 'e', 'i', 'o', 'u']
    return sum([count(n, vowel) for vowel in vowels])


if __name__ == '__main__':
    n = 1
    assert countVowelStrings(n) == 5
    n = 2
    assert countVowelStrings(n) == 15
    n = 33
    assert countVowelStrings(n) == 66045
    print(countVowelStrings(n))
    n = 1
    print(countVowelStrings_dp(n))
    assert countVowelStrings_dp(n) == 5
    n = 2
    assert countVowelStrings_dp(n) == 15
    n = 33
    assert countVowelStrings_dp(n) == 66045
    print(countVowelStrings_dp(n))