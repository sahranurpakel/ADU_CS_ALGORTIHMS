# ! https://leetcode.com/problems/find-the-duplicate-number/
def find_duplicate(nums):
    nums.sort()
    left = 0

    while left < len(nums) - 1:
        if nums[left] == nums[left + 1]:
            return nums[left]
        left += 1

    return None

print(find_duplicate([1, 3, 4, 2, 2]))
