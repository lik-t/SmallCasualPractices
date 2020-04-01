import re

class Solution:

    def romanToInt(self, s) -> int:

        # transfer table
        trans = {
            'I': 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
        }

        sum = 0
        pre = 10000
        for car in s:
            val = trans[car]
            if pre < val:
                sum -= pre*2
            sum += val
            pre = val

        return sum

s = Solution()
ipt = "IV"
print(s.romanToInt(ipt))


        # transfer_table = {
        #     "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9,
        #     "X": 10, "XX": 20, "XXX": 30, "XL": 40, "L": 50, "LX": 60, "LXX": 70, "LXXX": 80, "XC": 90,
        #     "C": 100, "CC": 200, "CCC": 300, "CD": 400, "D": 500, "DC": 600, "DCC": 700, "DCCC": 800, "CM": 900,
        #     "M": 1000, "MM": 2000, "MMM": 3000
        # }

        # # In keys, 'N' could be any character except letters used to
        # # represent number in Roman.
        # keys = [('M', 'N'), ('C', 'D'), ('X', 'L'), ('I', 'V')]
        # r = 0
        # while s:
        #     key = keys.pop()
        #     idx_1 = s.find(key[0])
        #     idx_2 = s.find(key[1])
        #     # idx_1 == idx_2 means the digit is zero.
        #     # For example:
        #     # If both 'I' and 'V' do not appear, the rightmost digit is zero.
        #     # And now, idx_1 = idx_2 = -1. This holds for the 2nd and 3rd
        #     # rightmost digits.
        #     if idx_1 == idx_2:
        #         continue
        #     elif idx_1 == -1:
        #         r += transfer_table[s[idx_2:]]
        #         s = s[:idx_2]
        #     elif idx_2 == -1:
        #         r += transfer_table[s[idx_1:]]
        #         s = s[:idx_1]
        #     else:
        #         n = min(idx_1, idx_2)
        #         r += transfer_table[s[n:]]
        #         s = s[:n]

        # return r



# class Solution:
#     def romanToInt(self, s: str) -> int:
#         r = 0
#         if s.startswith('M'):
#             if s.startswith('MMM'):
#                 n = 3
#                 s = s[3:]
#             elif s.startswith('MM'):
#                 n = 2
#                 s = s[2:]
#             else:
#                 n = 1
#                 s = s[1:]
#         else:
#             n = 0
#         r = n

#         if s.startswith("C"):
#             if s.startswith("CCC"):
#                 n = 3
#                 s = s[3:]
#             elif s.startswith("CC"):
#                 n = 2
#                 s = s[2:]
#             elif s.startswith("CD"):
#                 n = 4
#                 s = s[2:]
#             elif s.startswith("CM"):
#                 n = 9
#                 s = s[2:]
#             else:
#                 n = 1
#                 s = s[1:]
#         elif s.startswith("D"):
#             if s.startswith('DCCC'):
#                 n = 8
#                 s = s[4:]
#             elif s.startswith('DCC'):
#                 n = 7
#                 s = s[3:]
#             elif s.startswith('DC'):
#                 n = 6
#                 s = s[2:]
#             elif s.startswith('D'):
#                 n = 5
#                 s = s[1:]
#         else:
#             n = 0
#         r = r*10 + n

#         if s.startswith("X"):
#             if s.startswith("XXX"):
#                 n = 3
#                 s = s[3:]
#             elif s.startswith("XX"):
#                 n = 2
#                 s = s[2:]
#             elif s.startswith("XL"):
#                 n = 4
#                 s = s[2:]
#             elif s.startswith("XC"):
#                 n = 9
#                 s = s[2:]
#             else:
#                 n = 1
#                 s = s[1:]
#         elif s.startswith("L"):
#             if s.startswith('LXXX'):
#                 n = 8
#                 s = s[4:]
#             elif s.startswith('LXX'):
#                 n = 7
#                 s = s[3:]
#             elif s.startswith('LX'):
#                 n = 6
#                 s = s[2:]
#             elif s.startswith('L'):
#                 n = 5
#                 s = s[1:]
#         else:
#             n = 0
#         r = r*10 + n

#         if s.startswith("I"):
#             if s.startswith("III"):
#                 n = 3
#                 s = s[3:]
#             elif s.startswith("II"):
#                 n = 2
#                 s = s[2:]
#             elif s.startswith("IV"):
#                 n = 4
#                 s = s[2:]
#             elif s.startswith("IX"):
#                 n = 9
#                 s = s[2:]
#             else:
#                 n = 1
#                 s = s[1:]
#         elif s.startswith("V"):
#             if s.startswith('VIII'):
#                 n = 8
#                 s = s[4:]
#             elif s.startswith('VII'):
#                 n = 7
#                 s = s[3:]
#             elif s.startswith('VI'):
#                 n = 6
#                 s = s[2:]
#             elif s.startswith('V'):
#                 n = 5
#                 s = s[1:]
#         else:
#             n = 0
#         r = r*10 + n

#         return r
