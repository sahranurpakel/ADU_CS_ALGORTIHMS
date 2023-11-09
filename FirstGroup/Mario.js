// ! https://cs50.harvard.edu/x/2020/psets/1/mario/less/
const mario = (number) => {
  for (let i = 0; i < number; i++) {
    for (let s = 0; s < number - i - 1; s++) {
      process.stdout.write(" ");
    }
    for (let j = 0; j <= i; j++) {
      process.stdout.write("#");
    }
    process.stdout.write("\n");
  }
};
mario(8);
