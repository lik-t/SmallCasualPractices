class Solution:
    def letterCombinations(self, digits):
        dgts2ltrs = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
                     '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return list(dgts2ltrs[digits])
        elif len(digits) == 2:
            ans = []
            for ltr in dgts2ltrs[digits[0]]:
                for elem in dgts2ltrs[digits[1]]:
                    ans.append(ltr+elem)
            return ans
        else:
            ans = []
            for ltr in dgts2ltrs[digits[0]]:
                for elem in self.letterCombinations(digits[1:]):
                    ans.append(ltr+elem)

            return ans

s = Solution()
ipt = "234"
print(s.letterCombinations(ipt))