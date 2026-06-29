class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies
        count = Counter(nums)

        # Bucket sort: index = frequency
        n = len(nums)
        bucket = [[] for _ in range(n + 1)]
        for num, freq in count.items():
            bucket[freq].append(num)

        # Collect top k from highest frequency buckets
        result = []
        for freq in range(n, 0, -1):
            for num in bucket[freq]:
                result.append(num)
                if len(result) == k:
                    return result
        return result   # fallback (should not be reached given constraints)