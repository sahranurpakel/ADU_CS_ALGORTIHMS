// ! https://leetcode.com/problems/binary-search/
var search = function (nums, target) {
  let left = 0;
  let right = nums.length;
  while (left <= right) {
    let mid = Math.floor(left + (right - left) / 2);
    if (nums[mid] === target) return mid;
    else if (target < nums[mid]) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
  return -1;
};
