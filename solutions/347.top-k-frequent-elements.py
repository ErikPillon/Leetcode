class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict([(i, nums.count(i)) for i in {*nums}])
        l = sorted(d.items(), key=lambda x:x[1], reverse=True)
        return [i[0] for i in l[:k]]        