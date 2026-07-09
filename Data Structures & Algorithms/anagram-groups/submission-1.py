class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        for word in strs:
            sorted_word = str(sorted(word))
            if sorted_word not in groups:
                groups[sorted_word] = []
                
            groups[sorted_word].append(word)
            


        return list(groups.values())

                

            
        