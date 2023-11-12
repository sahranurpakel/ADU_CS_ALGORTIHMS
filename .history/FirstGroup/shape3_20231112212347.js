const shape3 = (sayi) => {
  for (let i = 1; i <= sayi; i++) {
    process.stdout.write(`${i}`);
    for (let j = i + 1; j <= sayi; j++) {
      process.stdout.write(`${j}`);
    }
    // Buraya kadarki kısım
    // 1234
    // 234
    // 34
    // 4 çıktısını veriyor alttaki de yanlarına sayı ekliyor.
    for (let j = 1; j < i; j++) {
      process.stdout.write(`${j}`);
    }
    process.stdout.write("\n");
  }
};
shape3(4);
// 1234
// 2341
// 3412
// 4123
