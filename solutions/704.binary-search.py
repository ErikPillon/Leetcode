class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        if (target<nums[0] or target>nums[l-1]):
            return -1
        bottom = 0
        top = l
        while bottom != top:
            if nums[int((bottom+top)/2)] > target:
                top = int((bottom+top)/2)
            elif nums[int((bottom+top)/2)] < target:
                bottom = int((bottom+top)/2)+1
            else: 
                return int((bottom+top)/2)
        return -1