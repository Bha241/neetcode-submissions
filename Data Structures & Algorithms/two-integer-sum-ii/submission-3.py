class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l1 = {}
        for i,num in enumerate(numbers):
            comp = target - num
            if comp not in l1.keys():
                l1[num] = i+1
            else:
                return [l1[comp],i+1]


        