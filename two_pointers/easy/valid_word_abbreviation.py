class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0 
        j = 0
        while i < len(word)-1 and j <len(abbr) -1:
            print(word[i])
            print( word[j])
            if word[i] == abbr[j]:
                i+=1 
                j+=1
            elif abbr[j] == '0':
                return False
                break
            elif ord('0') <= ord(abbr[j]) <= ord('9') :
                print(abbr[j])
                num = ''
                while  ord('0') <= ord(abbr[j]) <= ord('9'):
                    num+= abbr[j]
                    j +=1
                i += int(num)
                if i>= len(word) or word[i] != abbr[j]: 
                    return False 
            else: 
                return False
                break
        return True