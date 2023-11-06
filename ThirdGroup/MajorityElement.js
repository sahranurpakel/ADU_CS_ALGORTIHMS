// ! https://leetcode.com/problems/majority-element/
var majorityElement = function (nums) {
  nums = nums.sort((a, b) => a - b);
  const c = Math.ceil(nums.length / 2);
  for (let i = 0; i <= nums.length - c; i++) {
    if (nums[i] === nums[i + c - 1]) {
      return nums[i];
    }
  }
};
console.log(majorityElement([3, 2, 3]));
