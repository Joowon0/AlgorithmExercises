## neighbors.py

In a two dimensional grid, you have non-negative integers. Fig. 1 shows an example of such grid. The bold numbers denotes x- and y-indexes of the grids. You can tell the location of a grid using the pair (a, b) where a and b denotes the x- and y-indexes respectively. For instance the location of 20 is (5, 2).

For an integer in this grid you can think of the eight neighbors of it. For example, for the integer 12 located at (4, 2), the neighbors are 2, 5, 8, 20, 5, 1, 3, and 9 located in the shaded grids.

For the location at the end, the whole grid is assumed to be surrounded by zeroes. For example, the grid in Fig. 1 is assumed as the grid in Fig. 2.   

Write a program to find the location where the sum of neighbors is the maximum. Your program should print the x- and y-indexes of the location separated by a space.

For the example case, your program should find the location (5, 3) where the sum of neighbors is 94 (12 + 20 + 3 + 8 + 11 + 30 + 9 + 1 = 94).

Input file contains the grids line by line starting from the y-index 0. Every input line contains the numbers, separated by space, starting from the x-index 0.

Your program should print the x- and y-indexes separated by a space. If there are multiple locations where the sums of neighbors are maximum, print the location whose y-index is the least. If the y-indexes of them are same, print the location whose x-index is the least.

INPUT | OUTPUT 
--- | ---
2 9 3 6 10 1 7 <br> 2 5 6 2 5 8 5 <br> 4 7 5 9 12 20 3 <br> 7 3 4 3 1 5 8 <br> 6 7 8 4 9 30 11 | 5 3
1 0 0 0 0 <br> 0 1 0 0 0 <br> 0 0 0 0 0 | 1 0