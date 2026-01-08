# link: https://neetcode.io/problems/anagram-groups/question?list=allNC
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst = []
        for i in range(len(strs)):
            lst_temp =[]
            check = True
            print(strs[i])
            for j in range(i+1,len(strs)):   
                if sorted(strs[i]) == sorted(strs[j]) and strs[i] != "":
                    check = False
                    if strs[i] not in lst_temp:
                        lst_temp.append(strs[i]) 
                    lst_temp.append(strs[j])
                    strs[j] =""
            if lst_temp == []:
                continue
            elif check is True or (strs[i] == len(strs) -1 and strs[i] !=""):
                lst_temp.append(strs[i]) 
            lst.append(lst_temp)           
        return lst