class Solution:
    def maxArea(self, height: List[int]) -> int:
        right = len(height)-1
        left = 0
        ans = min(height[right], height[left])*(right-left)
        while right>left:
            if height[right] > height[left]:
                left +=1
                water = min(height[right], height[left])*(right-left)
                ans = max(water, ans)
            else:
                right -= 1
                water = min(height[right], height[left])*(right-left)
                ans = max(water, ans)
        return ans