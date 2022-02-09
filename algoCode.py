from collections import Counter


# Complete the 'printEven' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER N as parameter.


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
            max_profit, min_price = 0, float('inf')
            for price in prices:
                min_price = min(min_price, price)
                #sec_min_price = min((x for y in prices))
                profit = price - min_price
                max_profit = max(max_profit, profit)

            return max_profit
            

################################################################################

# Given an array of integers nums and an integer target, return indices
# of the two numbers such that they add up to target.

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i

#################################################################################

#Given an integer x, return true if x is palindrome integer.
#An integer is a palindrome when it reads the same backward as forward.

    def isPalindrome(self, x: int) -> bool:
        x_forward = str(x)
        x_back = str(x)
        x_back1 = x_back[::-1]
        if x_forward == x_back1:
            return True
        else:
            False

#if __name__ == '__main__':


#################################################################################

# Given two strings s and p, return an array of all the start indices of p's
# anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly once.


    def findAnagrams(self, s: str, p:str) -> list[int]:
        res = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p)-1])
        for i in range(len(p)-1, len(s)):
            sCounter[s[i]] += 1 # include a new char in the window
            if pCounter == sCounter: # This step is O(1), since there are at most 26 English Letters
                res.append(i-len(p)+1)  # append the starting index
            sCounter[s[i - len(p)+1]] -= 1 # decrease the count of the oldest char in the window
            if sCounter[s[i - len(p)+1]] == 0:
                del sCounter[s[i - len(p)+1]]
        return res


        # for every letter in p
        # if letter in p and next p        

    

# ^^^^^^Practice this ROLLING WINDOW ALGORITHM because very important algorithm!!!!!!!!!!!!!!!

    def addDigits(self, num: int) -> int:
        if num == 0: return 0
        else: return (num-1) % 9 +1

if __name__ == '__main__':
    soln = Solution()
    prices = [7,1,5,3,6,4]
    result = soln.maxProfit(prices)
#
#    result1 = str(result)
#    print(f'{result1} \n')

#    x = 121
#    result = isPalindrome(x)
    print(f'The result is {result}')

    s = 'abab'
    p = 'ab'
    
    final_soln = soln.findAnagrams(s,p)
    print(final_soln)



    num = 38
    final_soln1 = soln.addDigits(num)
    print(final_soln1)