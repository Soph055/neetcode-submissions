class Solution:
    def reverseString(self, s: List[str]) -> None:
       l = 0
       r = len(s) -1 

       while (l < r):
        temp = s[l]
        #swap
        s[l] = s[r]
        #other swap
        s[r] = temp
        l += 1
        r -= 1

        #DONE STRAIGHT FROM THE DOME O(n) O(1) AMAZING WORK
        #could also do s.reverse() 

        