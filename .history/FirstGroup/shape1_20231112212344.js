const shape1 = (sayi) => {
  let satir = 0;
  let sutun = 0;

  for (satir = 0; satir < sayi - 1; satir++) {
    for (sutun = 0; sutun < sayi - 1; sutun++) {
      if (satir === sutun) {
        process.stdout.write(" ");
      } else {
        process.stdout.write("#");
      }
    }
    process.stdout.write("\n");
  }
};
shape1(12);
// ##########
// # #########
// ## ########
// ### #######
// #### ######
// ##### #####
// ###### ####
// ####### ###
// ######## ##
// ######### #
// ##########
