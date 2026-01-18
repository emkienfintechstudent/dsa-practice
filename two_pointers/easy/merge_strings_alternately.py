class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1)<=len(word2): 
            loop = len(word1)
        else: loop = len(word2)
        str = ''
        for i in range(loop):
            str += word1[i]
            str += word2[i]
        if len(word1) <len(word2):
            str += word2[loop:]
        elif  len(word1) >len(word2):
            str += word1[loop:]
        return str