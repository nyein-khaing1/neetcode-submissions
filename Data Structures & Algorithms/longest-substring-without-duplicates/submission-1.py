#1. Repeat the problem
#I’m given a string, and I need to find the length of the longest substring that contains no repeated characters.
# for example:abca

#2. Clarify anything important
#Can the string be empty?
#Can it contain spaces or other characters?

#3. Simple approach first
#The brute-force approach would be to generate every possible substring and check whether each substring contains duplicate characters.
#That would be inefficient because there are many possible substrings, so I’d like to avoid checking all of them.

#4. Better approach — Sliding Window
#I can use a sliding window with two pointers, left and right, and a set to keep track of the characters currently inside the window.
#As I move the right pointer through the string, if the new character is not already in the set, I add it and update the longest length.
#If the character is already in the set, I shrink the window from the left. I remove characters from the set and move the left pointer until the duplicate is gone.
#Once the window contains only unique characters again, I can continue expanding it


##The time complexity is O(n). Even though there is a while loop inside the for loop, each character is added to the set at most once and removed at most once.
#The space complexity is O(n) in the worst case, because if every character is unique, the set could contain all characters.






class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        #This set stores the characters currently inside my     sliding window.
        l = 0
        res = 0
        for r in range(len(s)):
        #The right pointer moves through the string one character at a time.
            while s[r] in charSet:
            #If the current character is already in my window, I need to shrink the window until that duplicate is removed
                charSet.remove(s[l])
                l += 1
                #I remove the leftmost character from the set and move the left pointer forward
            charSet.add(s[r])
            #Now the current character is safe to add.
            res = max(res, r - l + 1)
            #The current window length is right - left + 1, and I keep the largest value seen so far.
        return res


        