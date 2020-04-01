
class Solution:

    def maxArea(self, height) -> int:
        mx = 0
        j = 1
        k = -1
        while k-j > 0:
            if height[j-1] <= height[k-1]:
                mx = max(mx, (k-j)*height[j-1])
                j += 1
            else:
                mx = max(mx, (k-j)*height[k-1])
                k -= 1

        return mx


s = Solution()
hh = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(s.maxArea(hh))

