class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        empty_list = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in empty_list:
                empty_list[sorted_word].append(word)
            if sorted_word not in empty_list:
                empty_list[sorted_word] = [word]
        return  list(empty_list.values())
        

        