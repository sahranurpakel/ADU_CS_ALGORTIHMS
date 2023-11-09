//  ! https://csacademy.com/ieeextreme-practice/task/lemons/
let lemons = (N, M, S) => {
  let medium = 1;
  let count = 0;
  while (medium <= N) {
    medium = Math.floor((medium + N) / 2);
    medium = medium + 1;
    count++;
  }
  return count * S + (N - 1) * M;
};
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (input) => {
  const [N, M, S] = input.split(" ").map(Number);
  console.log(lemons(N, M, S));
  rl.close();
});
