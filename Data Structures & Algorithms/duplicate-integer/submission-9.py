class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        empty_set = set()
        for num in nums:
            empty_set.add(num)
        
        if len(empty_set)<len(nums):
            return(True)
        else:
            return(False)
                
            