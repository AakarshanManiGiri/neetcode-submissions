class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nummap = set()
        for num in nums:
            if num in nummap:
                return True
            nummap.add(num)
        return False
            
        
        