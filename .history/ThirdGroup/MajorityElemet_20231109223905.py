# ! https://leetcode.com/problems/majority-element/
def majority_element(nums):
    nums.sort()
    c = len(nums) // 2 + 1
    for i in range(len(nums) - c + 1):
        if nums[i] == nums[i + c - 1]:
            return nums[i]

result = majority_element([3, 2, 3])
print(result)
