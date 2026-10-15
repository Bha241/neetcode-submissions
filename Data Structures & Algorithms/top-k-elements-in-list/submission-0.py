class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        top_k = []
        for num in nums:
            if num in freq:
                freq[num] +=1
            else :
                freq[num] = 1
        freq_sorted = sorted(freq.items(), key=lambda item: item[1],reverse = True)
        return [num for num,count in freq_sorted[:k]]

        