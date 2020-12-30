class Solution:
    def productExceptSelf1(self, nums):
        length = len(nums)
        left_product = [0] * length
        right_product = [0] * length
        # Left Product
        left_product[0] = 1
        for i in range(1, length):
            left_product[i] = left_product[i-1] * nums[i-1]
        # Right Products
        right_product[-1] = 1
        i = length - 2
        while i >= 0:
            right_product[i] = right_product[i+1] * nums[i+1]
            i -= 1
        answer = [0] * length
        for j in range(length):
            answer[j] = left_product[j] * right_product[j]
        return answer

    def productExceptSelf2(self, nums):
        length = len(nums)
        answer = [0] * length

        answer[0] = 1
        for i in range(1, length):
            answer[i] = answer[i-1] * nums[i-1]

        R = 1
        for i in reversed(range(length)):
            answer[i] = answer[i] * R
            R *= nums[i]
        return answer
nums = [1, 2, 3, 4]
sol = Solution()
print(sol.productExceptSelf1(nums))
print(sol.productExceptSelf2(nums))
