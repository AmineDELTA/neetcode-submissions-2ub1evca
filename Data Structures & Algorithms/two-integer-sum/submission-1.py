class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Prevset = {}

        for i, v in enumerate(nums):
            diff = target - v
            if diff in Prevset:
                return [Prevset[diff], i]
            Prevset[v] = i
        return



            

        