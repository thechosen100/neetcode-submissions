class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l2 = []
        for i in nums:
            if i not in l2:
                l2.append(i)
            else:
                return True
        return False