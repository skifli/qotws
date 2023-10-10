## [INTERMEDIATE PART 1]

Write a function that takes in a corner flag **(TOP_LEFT, TOP_RIGHT, BOTTOM_RIGHT, BOTTOM_LEFT)** and outputs the taxicab distance to that corner from the nearest L character.

For example, if the nearest L was at zero-indexed co-ords `(2, 1)`, taxicab to TOP_LEFT (0, 0) would be `(2 - 0) + (1 - 0) = 3`.

Find the sum of the outputs for each corner of grid.txt.

## [INTERMEDIATE PART 2]

How many L characters do not border any S characters? Use **orthogonal adjacency** - i.e., diagonals are not borders.