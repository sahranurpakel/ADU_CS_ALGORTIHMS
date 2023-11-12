// ! https://leetcode.com/problems/find-the-duplicate-number/
var findDuplicate = function (nums) {
  let left = 0;
  nums = nums.sort((a, b) => a - b);
  while (left - 1 < nums.length) {
    if (nums[left] === nums[left + 1]) {
      return nums[left];
    }
    left++;
  }
  return;
};
console.log(findDuplicate([1, 3, 4, 2, 2]));
// Başk abir çözüm : {} yapısı unique key kabul eder bundan faydalanarak aslında kontrol sağlıyoruz.
// var findDuplicate = function (arr) {
//   let hashmap = {};
//   for (var i = 0; i < arr.length; i++) {
//     console.log(hashmap[arr[i]]);
//     if (arr[i] in hashmap) {
//       return arr[i];
//     } else {
//       hashmap[arr[i]] = i;
//     }
//   }
// };
