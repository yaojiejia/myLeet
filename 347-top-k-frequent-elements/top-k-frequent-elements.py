class Solution(object):
    def topKFrequent(self, nums, k):
        result = {}
        for num in nums:
            if num in result:
                result[num] += 1
            else:
                result[num] = 1
        
        sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)
        top_k = [item[0] for item in sorted_result[:k]]
        return top_k


        