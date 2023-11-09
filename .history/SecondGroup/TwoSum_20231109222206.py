def two_sum(nums, target)
    num_indices = {}

    for index, num in enumerate(nums)
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], index]
        
        num_indices[num] = index
    
    return None

nums = [2, 7, 11, 15]
target = 9

result = two_sum(nums, target)

print("Çözüm indisleri:", result)
