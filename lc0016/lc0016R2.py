import bisect

class Solution:
    def threeSumClosest(self, nums, target) -> int:
        if len(nums) < 3:
            return None

        nums.sort()

        closest_dis = abs(nums[0]+nums[1]+nums[-1]-target)
        closest_sum = nums[0]+nums[1]+nums[-1]

        for idx, val in enumerate(nums[:-2]):
            if target - val - nums[-1] in nums[idx+1:-1]:
                return target
            else:
                pos = bisect.bisect_left(nums[idx+1:-1], val)
                if abs(val+nums[idx+1:-1][pos]+nums[-1]-target) < closest_dis:
                    closest_dis = abs(val+nums[idx+1:-1][pos]+nums[-1]-target)
                    closest_sum = val+nums[idx+1:-1][pos]+nums[-1]
                if abs(val+nums[pos+1]+nums[idx+1:-1][-1]-target) < \
                        closest_dis:
                    closest_dis = abs(val + nums[idx+1:-1][pos+1] + nums[-1] -
                                                 target)
                    closest_sum = val+nums[idx+1:-1][pos+1]+nums[-1]

        return closest_sum

s = Solution()
ipt1 = [0, 0, 0]
ipt2 = 1
print(s.threeSumClosest(ipt1, ipt2))