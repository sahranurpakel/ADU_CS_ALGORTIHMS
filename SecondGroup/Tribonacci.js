// https://leetcode.com/problems/n-th-tribonacci-number/
var tribonacci = function(n) {
    // Base case'leri kontrol et
    if (n === 0) return 0;
    if (n === 1 || n === 2) return 1;

    // Tribonacci dizisini hesapla
    let dp = [0, 1, 1];
    for (let i = 3; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
    }

    return dp[n];
};

// Örnek kullanım
const n = 4;
const result = tribonacci(n);
console.log(result); // Çıktı: 4
