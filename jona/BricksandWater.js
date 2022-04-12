export function bricksAndWater(bricksArray) {
  let water = 0;
  for (let i in bricksArray) {
    for (let j = i; j <= bricksArray.length; j++) {
      for (let k = i; k <= j; k++) {
        if (
          bricksArray[i] > bricksArray[k] &&
          bricksArray[j] > bricksArray[k]
        ) {
          water += Math.min(bricksArray[i], bricksArray[j]) - bricksArray[k];
          bricksArray[k] = Math.min(bricksArray[i], bricksArray[j]);
        }
      }
    }
  }
  return water;
}
