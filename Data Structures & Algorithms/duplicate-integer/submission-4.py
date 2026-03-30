class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
     hash={}
     for each in nums:
        if each in hash:
            return True
        else:
            hash[each]=1
     return False