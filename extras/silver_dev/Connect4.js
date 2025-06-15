function Connect4(movements = []) {
  this.grid = Array.from({ length: 6 }, (x) => (x = new Array(7).fill(0)));
  this.player = 1;
  this.winner = null;

  this.play = function (col) {
    for (let i = this.grid.length - 1; i >= 0; i--) {
      if (this.grid[i][col] === 0) {
        this.grid[i][col] = this.player;
        const winner = this.checkWinner(i, col);
        if (winner) {
          console.log(`Player ${winner} wins`);
          this.winner = winner;
          break;
        }
        this.player = this.player === 1 ? 2 : 1;
        break;
      }
    }
  };

  this.print = function () {
    console.table(this.grid);
  };

  const checkDirection = function (row, col, dr, dc) {
    let count = 0;
    let r = row + dr;
    let c = col + dc;

    while (
      r >= 0 &&
      r < this.grid.length &&
      c >= 0 &&
      c < this.grid[0].length &&
      this.grid[r][c] === this.player
    ) {
      count++;
      r += dr;
      c += dc;
    }

    return count;
  }.bind(this);

  this.checkWinner = function (row, col) {
    const deltas = [
      [1, 0],
      [0, 1],
      [1, 1],
      [-1, 1],
    ];

    for (let [dr, dc] of deltas) {
      let count = 1;
      count += checkDirection(row, col, dr, dc);
      count += checkDirection(row, col, -dr, -dc);

      if (count >= 4) {
        return this.player;
      }
    }
    return 0;
  };

  for (let col of movements) {
    this.play(col);
  }
}

(() => {
  const tcs = [
    // 0. Vertical win in leftmost column
    [0, 1, 0, 1, 0, 1, 0],

    // 1. Vertical win in rightmost column
    [6, 5, 6, 5, 6, 5, 6],

    // 2. Horizontal win starting from column 3
    [3, 0, 4, 0, 5, 0, 6],

    // 3. Horizontal win starting from column 0
    [0, 4, 1, 4, 2, 4, 3],

    // 4. Diagonal "\" from bottom-left to top-right
    [0, 1, 1, 2, 2, 3, 2, 3, 3, 6, 3],

    // 5. ❌ REPLACED (was Player 2 win), now diagonal "/" for Player 1
    [3, 2, 2, 1, 1, 0, 1, 0, 0, 6, 0],

    // 6. Diagonal "\" near right edge
    [3, 4, 4, 5, 5, 6, 5, 6, 6, 0, 6],

    // 7. Diagonal "/" near left edge (same as new 5, ok to keep for variety)
    [3, 2, 2, 1, 1, 0, 1, 0, 0, 6, 0],

    // 8. Full board draw (no winner)
    [
      0, 1, 0, 1, 0, 1, 2, 2, 3, 2, 3, 2, 3, 4, 4, 5, 4, 5, 4, 5, 6, 6, 0, 6, 0,
      6, 0, 1, 1, 2, 1, 2, 1, 2, 3, 3, 4, 3, 4, 3, 4, 5, 5, 6, 5, 6, 5, 6,
    ],

    // 9. Top row horizontal win for Player 1
    [0, 1, 0, 1, 0, 1, 0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 3, 1, 3, 1, 3, 1, 3], // Corrected version
  ];

  for (let i = 0; i < tcs.length; i++) {
    const game = new Connect4(tcs[i]);
    game.print();
    if (i === 8) {
      console.assert(game.winner === 0, `Test case ${i} should be a draw`);
    } else {
      console.assert(
        game.winner === 1,
        `Test case ${i} should be won by player 1`,
      );
    }
  }
})();
