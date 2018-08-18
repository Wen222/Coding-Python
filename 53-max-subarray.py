#!/usr/bin/env python

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(5.0//2.0)
        print(5.0/2.0)
        
        if not nums:
            return 0
        
        max_now = max_all_time = nums[0]
        
        if max(nums) <= 0:
            return max(nums)
        if len(nums)==2:
            return max(max(nums),sum(nums))
        
        for n in nums[1:]:
            max_now = max(n, max_now+n)
	    print(max_now)
            max_all_time = max(max_now, max_all_time)
            print(max_all_time)
        return max_all_time

if __name__ == "__main__":
    print(Solution().maxSubArray([8,-19,5,-4,20]))
