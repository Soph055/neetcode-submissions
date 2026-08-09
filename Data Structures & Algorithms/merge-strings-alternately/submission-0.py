class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
   #2 pointer solution 
   # PS: don't need to know which string is longest. 
   #idea append strings alternatly when 1 runs out just add the rest of both strings (1 will be "")
   #O(n+m) space and time. 
        i, j = 0, 0
        res = []
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        res.append(word1[i:])
        res.append(word2[j:])
        return "".join(res)







            