class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_hashmap = {}
        for i, num in enumerate(nums):
            diff = target-num 
            if diff in target_hashmap:
                return([target_hashmap[diff], i])
            target_hashmap[num] = i
        return