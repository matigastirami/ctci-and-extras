/*

function Connect4(arr = [], needed = 4, rows = 6, cols = 7) { 

  this.grid = Array.from({length: rows}, x => (x = new Array(cols).fill(0)))
  this.player = 1;
  this.winner = null;

  this.play = function(col) {
    if (this.winner) {
      return this.winner;
    }
    for (let i = this.grid.length - 1; i >= 0; i--) {
      if (this.grid[i][col] === 0) {
        this.grid[i][col] = this.player;
        const winner = this.checkWinner(i, col);
        if (winner) {
          this.winner = winner;
        }
        this.player = this.player === 1 ? 2 : 1;
        break;
      }
    }
  }

  this.print = function() {
    console.table(this.grid);
  }

  const checkDirection = function (row, col, dr, dc) {
    let count = 0;
    let r = row + dr;
    let c = col + dc;

    while(r >= 0 && r < this.grid.length && c >= 0 && c < this.grid[0].length && this.grid[r][c] === this.player) {
      count++;
      r += dr;
      c += dc;
    }

    return count;
  }.bind(this);

  // code goes here  
  this.checkWinner = function(row, col) {
    const deltas = [
      [1, 0],
      [0, 1],
      [-1, 1],
      [1, 1],
    ];

    for (let [dr, dc] of deltas) {
      let count = 1;
      count += checkDirection(row, col, dr, dc);
      count += checkDirection(row, col, -dr, -dc);

      if (count >= needed) {
        return String(this.player);
      }
    }
    return null;
  }
  
  for (let col = 0; col <= arr.length; col++) {
    this.play(arr[col]);
  }

  this.print();

  return this.winner || "0";

}
*/

function Connect4_3D(arr = [], needed = 4, rows = 4, cols = 4, height = 4) { 

  this.grid = Array.from(
    {length: rows}, 
    y => (y = Array.from({length: cols}, z => (z = new Array(height).fill(0)))));
  this.player = 1;
  this.winner = null;

  this.play = function(row, col) {
    if (this.winner) {
      return this.winner;
    }

    console.log(this.grid.length, this.grid[0].length, this.grid[0][0].length)
    for (let z = height - 1; z >= 0; z--) {
      if (this.grid[row][col][z] === 0) {
        this.grid[row][col][z] = this.player;
        const winner = this.checkWinner(row, col, z);
        if (winner) {
          this.winner = winner;
        }
        this.player = this.player === 1 ? 2 : 1;
        break;
      }
    }
  }

  this.print = function() {
    console.table(this.grid);
  }

  const checkDirection = function (row, col, height, dr, dc, dh) {
    let count = 0;
    let r = row + dr;
    let c = col + dc;
    let h = height + dh;

    while(
      r >= 0 && r < this.grid.length && 
      c >= 0 && c < this.grid[0].length && 
      h >= 0 && h < this.grid[0][0].length &&
      this.grid[r][c][h] === this.player
    ) {
      count++;
      r += dr;
      c += dc;
      h += dh;
    }

    return count;
  }.bind(this);

  // code goes here  
  this.checkWinner = function(row, col, height) {
    const deltas = [
      // any given floor
      [1, 0, 0],
      [0, 1, 0],
      [1, 1, 0],
      [-1, 1, 0],
      
      // any given walls
      [0, 0, 1],
      [0, -1, 1],
      [0, 1, 1],
      
      // any given diagonal
      [1, 1, 1],
      [1, -1, 1],
      [-1, 1, -1],
      [-1, 1, 1],
      [1, 0, 1],
      [-1, 0, 1],
    ];

    for (let [dr, dc, dh] of deltas) {
      let count = 1;
      count += checkDirection(row, col, height, dr, dc, dh);
      count += checkDirection(row, col, height, -dr, -dc, -dh);

      if (count >= needed) {
        return String(this.player);
      }
    }
    return null;
  }
  
  for (let pos = 0; pos < arr.length; pos++) {
    this.play(arr[pos][0], arr[pos][1]);
  }

  this.print();

  return this.winner || "0";

}
// [first , .... ,  last ]
// first < last   -> increasing order
// first > last   -> decreasing order
// first == last  -> check if there is something != to any of the extremes

console.log('Sample test passing: ' + (Connect4_3D([[0,1], [0,2], [0,1], [0,2], [0,1], [0,2], [0,1]]) == '1'));
   
// keep this function call here 
// console.log('Sample test passing: ' + (Connect4([3, 4, 3, 4, 3, 4, 3]) == '1'));
// console.log('Sample test passing: ' + (Connect4([3, 4, 3, 4, 3, 4, 2, 4]) == '2'));

/* do not remove this line: __internalTestCases__ */