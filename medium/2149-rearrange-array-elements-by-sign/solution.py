class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos = []
        neg = []
        new = []
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)    
        for i in range(len(pos)):
            new.append(pos[i])
            new.append(neg[i])
        return new    
