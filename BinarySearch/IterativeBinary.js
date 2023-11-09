// ! Binary Search temel kodu diyebiliriz.
const binarySearchIterative = (arr, data) => {
  let left = 0;
  let right = arr.length - 1;
  let mid = 0;
  while (left <= right) {
    mid = Math.floor((left + right) / 2);
    if (data === arr[mid]) return true;
    else if (data > arr[mid]) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return false;
};
let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
console.log(binarySearchIterative(arr, 4));
