
'''
Arrays & Hashing:
EASY
1. Contains Duplicate:
# QUESTION

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false

# SOLUTION

1. brute foce: 
check each number of array, 
compare it to ALL the nums in array

2. sorting: [1,1,2,3]
we'll only have to check adjacent values to know if they're duplicates

3. hashsets: #most efficient
create a hashset
ask if a num in nums is already in the hashset, 
if there is return true
if not add the num to hashset 

'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()
        for n in nums: 
            if n in hashset:
                return True
            hashset.add(n)
        return False
    



'''
Arrays & Hashing:
EASY
2. Valid Anagram: 

# QUESTION

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false

# SOLUTION

1. sorting: 
if the two strings are anagrams, sorting the strings should be equvialent. 

2. HashMaps:
check if length is same 
use hashmap, to count the occurance of a letter for both strings, if anagram they should be same


'''

# solution 1:

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)




# solution 2:
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # {'r': 1, 'c': 1, 'a': 1}
            countT[t[i]] = 1 + countT.get(t[i], 0) # {'c': 1, 'a': 1, 'r': 1}
        
        return countT == countS
    




'''
Arrays & Hashing:
EASY
3. Two Sum:

# QUESTION

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]


Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

# SOLUTION

1. brute force:
checking every combination in array

2. hashmap:
because we know they're two digits make the target,
so the diff between the target and one of the digit reveals the the other digit
so if we enumerate the nums array, we get both indexes and the numbers
then we check if the difference exists in the array

'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        """
        hashmap = {} #num: index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i] #returns indexes
            hashmap[n] = i 

    

