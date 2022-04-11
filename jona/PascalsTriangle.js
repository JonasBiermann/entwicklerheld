export function getPascalsTriangleRow(rowNumber) {
  let ar = [1, 1];
  function getPascalsTriangleRow1(rowNumber) {
    if (rowNumber > 2) {
      getPascalsTriangleRow1(rowNumber - 1);
    } else if (rowNumber == 0) {
      return [1];
    } else if (rowNumber == 1) {
      return [1, 1];
    }
    let tmp = [1];
    for (let i = 0; i < ar.length - 1; i++) {
      tmp.push(ar[i] + ar[i + 1]);
    }
    tmp.push(1);
    ar = tmp;
    return ar;
  }
  return getPascalsTriangleRow1(rowNumber);
}
