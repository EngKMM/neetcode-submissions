class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_counter={}
        for num in nums:
            if num not in frequency_counter:
                frequency_counter[num] = 1
            else:
                frequency_counter[num] += 1
        
        sorted_hashmap = {k: v for k, v in sorted(frequency_counter.items(), key=lambda item: item[1])}
        value_list = list(sorted_hashmap.keys())
        return(value_list[-k:])
        