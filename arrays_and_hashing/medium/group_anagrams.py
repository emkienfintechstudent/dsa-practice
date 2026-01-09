# link: https://neetcode.io/problems/anagram-groups/question?list=allNC
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst = []
        
        for i in range(len(strs)):
            if strs[i] is None:
                continue            
            lst_temp = [strs[i]]
            for j in range(i + 1, len(strs)):
                if strs[j] is not None and sorted(strs[i]) == sorted(strs[j]):
                    lst_temp.append(strs[j])
                    strs[j] = None  
            
            lst.append(lst_temp)
            
        return lst

            

