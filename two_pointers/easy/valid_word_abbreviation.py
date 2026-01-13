class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0 
        j = 0
        while i <= len(word)-1 and j <=len(abbr)-1:
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
                    if j > len(abbr) -1 : break
                    
                i += int(num)
                print(i)
                print(j)
             
                if i == len(word) and j ==len(abbr): 
                        return True
                elif i>= len(word): 
                    return False
                elif  word[i] != abbr[j]:
                    return False
            else: 
                return False
                break
        return True
    

#optimize code
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        m, n = len(word), len(abbr)
        
        while i < m and j < n:
            if abbr[j].isdigit():
                if abbr[j] == '0':  # Leading zeros are invalid
                    return False
                
                num = 0
                while j < n and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                
                i += num
                
            elif word[i] == abbr[j]:
                i += 1
                j += 1
                
            else:
                return False
        
        return i == m and j == n