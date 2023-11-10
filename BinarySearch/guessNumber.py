#  https://leetcode.com/problems/guess-number-higher-or-lower/
#  guess fonksiyonu keetcode tarafından veriliyor biz eklemiyoruz 
# Leetcode dışında bu problemi çalıştırırsak guess hata verecek 
import math
class Solution(object):
    def guessNumber(self ,n) :
        left = 0
        right = n
        while left <= right:
            mid = math.floor((left + right) / 2)
            if(guess(mid) == 0) : return int(mid)
            elif (guess(mid) == 1):
                left = mid + 1
            else : 
                right = mid - 1
        