const deneme = (nums, target) => {
  let right = nums.length - 1;
  let left = 0;
  let mid = 0;

  while (left <= right) {
    mid = Math.floor((left + right) / 2);
    if (nums[mid] === target) {
      return nums[mid];
    } else if (nums[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return "Aradağın değer yok";
};
console.log(deneme([1, 2, 3, 4, 5, 6], 9890898));
