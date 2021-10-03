class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = 0
        res = []
        while (i < len(nums)-1):
            i = i+1
            for n in nums:
                if (n + nums[i] == target):
                    res.append(j)
                    res.append(i)
                j = j+1
        return res

nums = [2,7,11,15]
target = 9

s = Solution
s.twoSum(nums, target)
