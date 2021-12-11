board = document.body.textContent.trim().split("\n").map(s => s.split("").map(n => +n))

l = board.length;
m = board[0].length;
d = [
  [-1, 0],
  [0, -1],
  [1, 0],
  [0, 1],
  [-1, -1],
  [1, 1],
  [-1, 1],
  [1, -1]
];

b = new Set()
s = 0

function* neighbors(i, j) {
  for (const [di, dj] of d) {
    if (i + di < l && i + di > -1 && j + dj < m && j + dj > -1 && !b.has(1000 * (i + di) + j + dj)) yield [i + di, j + dj]
  }
};


function p(i, j) {
  if (b.has(1000*i + j)) return;
  if (++board[i][j] > 9) {
    board[i][j] = 0;
    b.add(1000*i + j)
    for (const [_i, _j] of neighbors(i, j)) {
      p(_i, _j)
    }
  }
}

for (let k = 0; ; k++) {
  for (let i = 0; i < l; i++) {
    for (let j = 0; j < m; j++) {
			p(i, j)
    }
  }
  s += b.size
  if (k == 99) {
    console.log(`Part 1:`, s)
  }
  
  if (b.size == l*m) {
    console.log(`Part 2:`, k+1)
    break
  }

  b = new Set()
}
