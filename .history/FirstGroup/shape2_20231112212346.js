const shape2 = (sayi2) => {
  let satir = 0;
  let sutun = 0;
  if (sayi2 % 2 === 0) sayi2 -= 1;
  for (satir = 0; satir < sayi2; satir++) {
    for (sutun = 0; sutun < sayi2; sutun++) {
      if (satir === sutun || satir + sutun === sayi2 - 1) {
        process.stdout.write(" ");
      } else {
        process.stdout.write("*");
      }
    }
    process.stdout.write("\n");
  }
};
shape2(10);
//  *******
// * ***** *
// ** *** **
// *** * ***
// **** ****
// *** * ***
// ** *** **
// * ***** *
//  *******
// X shape
