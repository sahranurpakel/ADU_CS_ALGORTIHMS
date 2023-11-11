const bmi = (kilo, boy) => {
  let bmi = kilo / (boy * boy);
  if (bmi < 18.5) {
    return "Zayıf";
  } else if (bmi >= 18.5 && bmi < 24.9) {
    return "Normal";
  } else if (bmi >= 24.9 && bmi < 29.9) {
    return "Fazla Kilolu";
  } else {
    return "Obez";
  }
};
console.log(bmi(70, 1.6));
