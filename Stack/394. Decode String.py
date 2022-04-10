
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
        for char in s:
            if char.isnumeric():
                num = num*10 + int(char)
            elif char.isalpha():
                letter += char
            elif char == '[':
                nums.append(num)
                num = 0
                letters.append(letter)
                letter = ""
            elif char == ']':
                repeat = nums.pop()
                prev_letter = letters.pop()
                letter = prev_letter + repeat*letter
        return letter

if __name__ == "__main__":
    solution = Solution()
    s = "3[a2[c]]"
    print(solution.decodeString(s))