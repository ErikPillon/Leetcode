class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pre = 1
        post = 1
        sol = [1]*l
        for i in range(l):
            sol[i] *= pre
            pre *= nums[i]
            sol[l-1-i] *= post
            post *= nums[l-1-i]
            #print(sol)
        return sol