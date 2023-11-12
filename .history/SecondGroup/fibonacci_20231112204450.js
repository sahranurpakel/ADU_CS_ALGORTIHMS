const fibbonacci = (number) => {
  let a = 1;
  let b = 1;
  let f = 0;
  for (let i = 0; i < number; i++) {
    //  Su Gazoz mantığı burada anlatılacak !!!
    f = a + b;
    a = b;
    b = f;
    console.log(`${i + 3} terim :  :>> `, f);
  }
};
fibbonacci(12);
