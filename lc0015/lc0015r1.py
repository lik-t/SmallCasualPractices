# （1）如果数组长度小于3，直接返回[];
# （2）将数组排序
# （3）指针i从0开始直到最后一个负数，指针j从i+1开始，指针k从j+1开始，
# 指针搜到最后一个负数时，记住次数，i不用超过此数，而j从此数开始
#

class Solution():

    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()

        rst = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i >= 1:
                if nums[i] == nums[i-1]:
                    continue

            j = i + 1
            k = len(nums)-1
            while True:
                if j >= k:
                    break
                if j > i + 1 and nums[j] == nums[j-1]:
                    j += 1
                    continue
                if k < len(nums) - 1 and nums[k] == nums[k+1]:
                    k -= 1
                    continue
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    rst.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

        return rst


            # for k in reversed(range(0, len(nums))):
            #     if nums[k] < 0:
            #         break
            #     if k < len(nums) - 1:
            #         if nums[k] == nums[k+1]:
            #             continue
            #     if nums[i] + nums[k] < nums[i] or nums[i] + nums[k] > nums[k]:
            #         break
            #
            #     for j in range(i+1, k):
            #          if nums[j] == nums[j-1] and j-1 != i:
            #              continue
            #          if nums[j] > - nums[i] - nums[k]:
            #              break
            #          if nums[i] + nums[j] + nums[k] == 0:
            #              rst.append([nums[i], nums[j], nums[k]])

        return rst


s = Solution()
ipt = [-1,0,1,2,-1,-4]
print(s.threeSum(ipt))



# class Solution():
#
#     def twoNumsWithCertainSum(self, nums, val):
#         """
#         This function is to find all pairs in a lists of numbers, sum of
#         them equals to zero.
#         :param nums: list of numbers in ascending order
#         :return:
#         """
#         rst = set()
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == val:
#                     if val > 0:
#                         rst.add((-val, nums[i], nums[j]))
#                     else:
#                         rst.add((nums[i], nums[j], -val))
#                 if nums[i] + nums[j] > val:
#                     break
#
#         return rst
#
#     def searchPair(self, nums1, nums2):
#         """
#         This function is to find all lists with three elements, 1st of which is
#          from single and the rest two from double.
#         :param nums1: list of numbers, in ascending order
#         :param nums2: list of numbers, in ascending order
#         :return: [[],[],...]
#         """
#         rst = set()
#         for num in nums1:
#             rst.update(self.twoNumsWithCertainSum(nums2, -num))
#
#         return rst
#
#     def searchNeg(self, nums1, nums2):
#         rst = set()
#         for num in nums1:
#             for com in nums2:
#                 if num == -com:
#                     rst.add((num, 0, com))
#                 if num > -com:
#                     break
#         return rst
#
#     def partitionLst(self, nums):
#         """
#         Partition a ascending-ordered list of number into three lists:
#         # One contains only negative numbers;
#         # One contains only zeros;
#         # One contains only positive numbers.
#         :param nums:
#         :return:
#         """
#         minus_end = -1
#         plus_begin = len(nums)
#         for i in range(len(nums)):
#             if nums[i] < 0:
#                 minus_end = i
#             if nums[i] > 0:
#                 plus_begin = i
#                 break
#         return nums[:minus_end+1], nums[minus_end+1:plus_begin], \
#                nums[plus_begin:]
#
#     def threeSum(self, nums):
#         nums.sort()
#         rst = set()
#         minus, zero, plus = self.partitionLst(nums)
#
#         if plus:
#             rst.update(self.searchPair(plus, minus))
#
#         if minus:
#             rst.update(self.searchPair(minus, plus))
#
#         if len(zero) > 0:
#             rst.update(self.searchNeg(minus, plus))
#
#         if len(zero) >= 3:
#             rst.add((0, 0, 0))
#
#         rst = list(rst)
#         rst = [ list(it) for it in rst]
#
#         return rst

