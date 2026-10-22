# Longest Consecutive Sequence

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an unsorted array of integers `nums`, return *the length of the longest consecutive elements sequence.*

You must write an algorithm that runs in `O(n)` time.

 

**Example 1:**

```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

```

**Example 2:**

```
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

```

**Example 3:**

```
Input: nums = [1,0,1,2]
Output: 3

```

 

**Constraints:**

- 0 <= nums.length <= 105
- -109 <= nums[i] <= 109

## Solution

**Language:** Python  
**Runtime:** 77 ms (beats 10.82%)  
**Memory:** 32.7 MB (beats 92.66%)  
**Submitted:** 2026-10-22T18:49:33.363Z  

```py
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        count = 1
        maxx = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1]+1:
                count += 1
                
            else:
                count = 1
            maxx = max(maxx,count)    

        return maxx
```

---

[View on LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/)