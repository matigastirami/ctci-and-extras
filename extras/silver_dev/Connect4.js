class Connect4 {
  // grid
  // player
  // winner (player)
  // play
  // checkWinner
  // print
  constructor() {
    this.grid = Array.from({ length: 6 }, (x) => (x = new Array(7).fill(0)));
    this.player = 1;
  }

  play(col) {
    for (let i = this.grid.length - 1; i >= 0; i--) {
      if (this.grid[i][col] === 0) {
        this.grid[i][col] = this.player;
        this.checkWinner(i, col, this.player);
        this.player = 3 - this.player;
        break;
      }
    }
  }

  checkWinner(row, col, player) {
    const offset = 3;
    let count = 0;
    for (let i = row - offset; i <= row + offset; i++) {
      if (i < 0 || i >= this.grid.length) continue;
      if (this.grid[i][col] === player) {
        count++;
        if (count === 4) {
          console.log(`The winner is player ${player}`);
          this.winner = player;
          return;
        }
      } else {
        count = 0;
      }
    }

    // check horizontal
    count = 0;
    for (let j = col - offset; j <= col + offset; j++) {
      if (this.grid[row][j] === player) {
        count++;
        if (count === 4) {
          console.log(`The winner is player ${player}`);
          this.winner = player;
          return;
        }
      } else {
        count = 0;
      }
    }

    // check diagonal \
    count = 0;
    for (let i = -offset; i <= offset; i++) {
      const r = row + i;
      const c = col + i;

      if (r < 0 || r >= this.grid.length || c < 0 || c >= this.grid[0].length)
        continue;

      if (this.grid[r][c] === player) {
        count++;

        if (count === 4) {
          console.log(`The winner is player ${player}`);
          this.winner = player;
          return;
        }
      } else {
        count = 0;
      }
    }

    // check diagonal /
    count = 0;
    for (let i = -offset; i <= offset; i++) {
      const r = row - i;
      const c = col + i;

      if (r < 0 || r >= this.grid.length || c < 0 || c >= this.grid[0].length)
        continue;

      if (this.grid[r][c] === player) {
        count++;

        if (count === 4) {
          console.log(`The winner is player ${player}`);
          this.winner = player;
          return;
        }
      } else {
        count = 0;
      }
    }

    return 0;
  }

  print() {
    console.table(this.grid);
  }
}

// keep this function call here
const game = new Connect4();
// vertical winner
// game.print();
// game.play(1);
// game.play(2);
// game.play(1);
// game.play(2);
// game.play(1);
// game.play(2);
// game.play(1);
// game.print();
// console.log(game.checkWinner(1, 1));

// horizontal winner
// game.play(1);
// game.play(1);
// game.play(2);
// game.play(2);
// game.play(3);
// game.play(3);
// game.play(5);
// game.play(4);
// game.play(5);
// game.play(4);
// game.print();

// vertical /
// game.play(0);
// game.play(1);
// game.play(1);
// game.play(2);
// game.play(3);
// game.play(2);
// game.play(2);
// game.play(3);
// game.play(3);
// game.play(4);
// game.play(3);
// game.print();

// vertical \
game.play(6);
game.play(5);
game.play(5);
game.play(4);
game.play(4);
game.play(3);
game.play(4);
game.play(3);
game.play(3);
game.play(0);
game.play(3);
game.print();

// Input: [3, 4, 3, 4, 3, 4, 3];
// Output: 1;

// Input: [3, 4, 3, 4, 3, 4, 2, 4];
// Output: 2;
