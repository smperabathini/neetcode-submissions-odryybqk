class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        buckets = [[] for i in range(len(nums)+1)]
        hm = defaultdict(int)
        for num in nums:
            hm[num] +=1
        for key, v in hm.items():
            print(v)
            buckets[v].append(key)
        for i in range(len(nums), -1, -1):
            if k == 0:
                return res
            for num in buckets[i]:
                res.append(num)
                k -= 1
        return res
            


