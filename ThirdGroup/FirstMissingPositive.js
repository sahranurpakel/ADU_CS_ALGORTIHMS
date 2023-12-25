//https://leetcode.com/problems/first-missing-positive/
var firstMissingPositive = function(nums) {
    // Dizi sıralanır
    nums.sort((a, b) => a - b);

    // Eksik olan en küçük pozitif tamsayıyı bulmak için dizi üzerinde dolaşılır
    let missing = 1;
    for (const num of nums) {
        if (num === missing) {
            missing++;
        } else if (num > missing) {
            // Eğer num, eksik sayıdan büyükse bulunmuştur, döngüyü sonlandırabiliriz
            break;
        }
    }

    return missing;
};

// Örnek kullanım
const nums = [3, 4, -1, 1];
const result = firstMissingPositive(nums);
console.log(result); // Çıktı: 2
