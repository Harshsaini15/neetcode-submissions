class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            
        
        freq_buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in count.items():
            freq_buckets[freq].append(num)
            
        
        res = []
        for i in range(len(freq_buckets) - 1, 0, -1):
            for n in freq_buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
