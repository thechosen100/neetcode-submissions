class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {}

        for i, n in enumerate(nums): #for all index and numbers to that index in nums
            diff = target - n #calc difference
            if diff in prevmap: #if that difference is in the prevmap dictionary
                return [prevmap[diff], i] #return the difference index (becuz prev map is {i:n})
            prevmap[n] = i #if nothing is returned then difference didnt exist so you add it to prevmap dictionary