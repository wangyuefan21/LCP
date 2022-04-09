class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        nums = []
        letters = []
        num = 0
        letter = ""
        ans = ""
        i = 0
        while i < len(s):
            print(i, s[i], nums, letters, num, letter, ans)
            while i < len(s) and s[i].isnumeric():
                num = num*10 + int(s[i])
                i += 1
            while i < len(s) and s[i].isalpha():
                letter += s[i]
                i += 1
            if i < len(s) and s[i] == '[':
                if num != 0:
                    nums.append(num)
                    num = 0
                if letter != "":
                    if letters:
                        letter = letters.pop() + letter
                    letters.append(letter)
                    letter = ""
                i += 1
            elif i < len(s) and s[i] == ']':
                repeat = nums.pop()
                if letter == "":
                    letter = letters.pop()
                temp_letter = repeat*letter
                if nums:
                    if letters and len(letters) == len(nums):
                        temp_letter = letters.pop() + temp_letter
                    letters.append(temp_letter)
                else:
                    ans += temp_letter
                letter = ""
                i += 1
        if letters:
            ans = letters[0] + ans
        return ans + letter

if __name__ == "__main__":
    solution = Solution()
    s = "3[a2[c]]"
    print(solution.decodeString(s))