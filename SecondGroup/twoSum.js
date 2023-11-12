const twoSum = (nums, target) => {
  let hashmap = {};
  let complement;
  for (let i = 0; i < nums.length; i++) {
    complement = target - nums[i];
    if (complement in hashmap) {
      return [hashmap[complement], i];
    }
    hashmap[nums[i]] = i;
  }
  return -1;
};
