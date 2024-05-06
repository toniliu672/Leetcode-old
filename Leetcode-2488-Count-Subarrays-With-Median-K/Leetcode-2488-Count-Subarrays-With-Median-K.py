class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict

        # Ubah array sesuai dengan petunjuk
        for i in range(len(nums)):
            if nums[i] < k:
                nums[i] = -1
            elif nums[i] > k:
                nums[i] = 1
            else:
                nums[i] = 0

        k_pos = nums.index(0)

        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        sum = 0
        for num in nums[k_pos+1:]:
            sum += num
            prefix_sum[sum] += 1

        res = prefix_sum[0] + prefix_sum[1]
        sum = 0
        for num in reversed(nums[:k_pos]):
            sum += num
            res += prefix_sum[-sum] + prefix_sum[1-sum]

        return res
