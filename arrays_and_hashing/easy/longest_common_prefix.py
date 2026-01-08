# link: https://neetcode.io/problems/longest-common-prefix/question
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        text =""
        index = 0
        if len(strs) ==1:
            return strs[0]
        else:
            while index<len(strs[0]):
                check = False
                for i in strs[1::]:
                    if len(i)-1 < index:
                        check = False
                        break
                    if i[index] == strs[0][index]:
                        check = True
                    else:
                        check = False
                        break
                if check is False:
                    break
                else:
                        text += i[index]
                        index +=1
        return text

# Solution
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         prefix = strs[0]
#         for i in range(1, len(strs)):
#             j = 0
#             while j < min(len(prefix), len(strs[i])):
#                 if prefix[j] != strs[i][j]:
#                     break
#                 j += 1
#             prefix = prefix[:j]
#         return prefix