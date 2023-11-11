const perfect = (number) => {
  let bolenler = 1;
  for (let i = 2; i < number; i++) {
    if (number % i === 0) {
      bolenler += i;
    }
  }
  if (bolenler === number) return "Perfect Number !";
  else {
    return "Perfect Değil...";
  }
};
console.log(perfect(7));
