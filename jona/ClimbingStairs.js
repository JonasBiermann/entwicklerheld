export function climbingStairs(numberOfStairs) {
  let res = 0;
  if (numberOfStairs < 1) {
    return 0;
  } else {
    function ways(nos) {
      if (nos > 1) {
        ways(nos - 2);
      }
      if (nos > 0) {
        ways(nos - 1);
      } else {
        res += 1;
      }
    }
    ways(numberOfStairs);
    return res;
  }
}
