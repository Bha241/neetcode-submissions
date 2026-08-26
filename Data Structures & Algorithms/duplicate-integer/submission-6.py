class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq_nums = []

        if len(nums) <= 1:
            return False
            
        for i in range(len(nums)):
            if nums[i] in uniq_nums :
               return True
            else :
                uniq_nums.append(nums[i])
        
        return False