class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        working_set = []
        for i in nums:
            if i in working_set:
                return True
            elif i not in working_set:
                working_set.append(i)
                continue
        return False
                