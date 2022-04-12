import Position from "./Position";

export function isSafeRook(positions, rook) {
  let isOk = true;
  positions.forEach(function (item) {
    if (
      item.rowIndex == rook.rowIndex ||
      item.columnIndex == rook.columnIndex
    ) {
      isOk = false;
      return;
    }
  });
  return isOk;
}

export function isSafeQueen(positions, queen) {
  let isOk = true;
  isOk = isSafeRook(positions, queen);
  positions.forEach(function (item) {
    if (
      item.leftDiagonal == queen.leftDiagonal ||
      item.rightDiagonal == queen.rightDiagonal
    ) {
      isOk = false;
      return;
    }
  });
  return isOk;
}

export function getQueensProblemSolution(boardSize) {
  if (boardSize < 4) {
    return [];
  }
  let x = [];
  let fini = true;

  function test(row, pos) {
    if (row < boardSize && fini) {
      for (let col = 0; col < boardSize; col++) {
        const tmp = new Position(row, col);
        if (isSafeQueen(pos, tmp)) {
          pos.push(tmp);
          test(row + 1, pos);
          pos.pop();
        }
      }
    } else if (pos.length == boardSize) {
      x = pos.slice();
      fini = false;
    }
  }
  test(0, []);
  return x;
}
