export function isCompletable(numbers) {
  let is = false;
  function check(index) {
    if (index < numbers.length) {
      if (index == numbers.length - 1) {
        is = true;
      }
      for (let i = 1; i <= numbers[index]; i++) {
        check(index + i);
      }
    }
  }
  check(0);
  return is;
}

export function getMinimalNumberOfJumps(numbers) {
  let minNum = numbers.length;
  function jumps(index, num) {
    if (index < numbers.length) {
      if (index == numbers.length - 1 && num < minNum) {
        minNum = num;
        num = 0;
      }
      for (let i = 1; i <= numbers[index]; i++) {
        jumps(index + i, num + 1);
      }
    }
  }
  jumps(0, 0);
  if (minNum == numbers.length) {
    return 0;
  }
  return minNum;
}
