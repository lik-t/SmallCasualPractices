class Solution:
    def threeSumClosest(self, nums, target) -> int:
        if len(nums) < 3:
            return None

        nums.sort()

        closet_sum = nums[0] + nums[1] + nums[-1]
        closet_dis = abs(closet_sum - target)

        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while True:
                new_sum = nums[i] + nums[j] + nums[k]
                new_dis = abs(new_sum - target)
                if new_dis < closet_dis:
                    closet_dis = new_dis
                    closet_sum = new_sum
                if new_sum == target:
                    return target
                elif new_sum > target:
                    k -= 1
                else:
                    j += 1

                if j >= k:
                    break

        return closet_sum

s = Solution()
ipt1 = [-1, 2, 1, -4]
ipt2 = 1
print(s.threeSumClosest(ipt1,ipt2))