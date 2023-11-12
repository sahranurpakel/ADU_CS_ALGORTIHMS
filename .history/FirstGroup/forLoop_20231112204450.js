for (let i = 1; i <= 10; i++) {
  process.stdout.write(`${i} __ \t`);
  for (let j = 30; j < 40; j++) {
    process.stdout.write(`a`);
  }
  process.stdout.write(`\n`);
}
