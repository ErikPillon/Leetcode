class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        ind = len(digits)-1
        while digits[ind] == 9 and ind>=0:
            digits[ind] = 0
            ind -= 1
        if ind == -1:
            digits.insert(0, 1)
        else:
            digits[ind] += 1
        return digits