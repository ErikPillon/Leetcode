class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        current_num = None
        nums_set = set(nums)
        for num in nums_set:
            if num-1 not in nums_set:
                current_num = num
                current = 1

                while current_num+1 in nums_set:
                    current_num += 1
                    current += 1

                longest = max(current, longest)
        return longest