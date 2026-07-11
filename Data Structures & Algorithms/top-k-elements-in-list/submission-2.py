class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        frequency=[[] for i in range(len(nums)+1)]
        for num in nums:
            count[num]=1+count.get(num,0)
        for num,count in count.items():
            frequency[count].append(num)
        
        results=[]
        for i in range(len(frequency)-1,0,-1):
            for n in frequency[i]:
                results.append(n)
                if len(results)==k:
                    return(results)
            
        