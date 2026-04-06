from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        distinct = list(freq.keys())
        distinct.sort(key=lambda x: freq[x],reverse=True)
        return distinct[:k]


        
        