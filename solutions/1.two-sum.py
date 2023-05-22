class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for ind, elem in enumerate(nums):
            if target-elem in nums[ind+1:]:
                return [ind, nums.index(target-elem, ind+1)]        
