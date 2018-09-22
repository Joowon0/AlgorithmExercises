## point.py

Write a program printing the farthest point from the origin in the two dimensional Cartesian plain. The distance of two points are measured by the Euclidian distance. You should use the function math.sqrt() to calculate the distance of two points.

Define a class Point with the constructor and dist method. The class Point should include __str__ method for the string representation.

In the input file, the x- and the y-coordinates of points are given line by line. Each line contains the x- and the y-coordinates of each point separated by a space. Your program should print the point farthest from the origin in the form of (X,Y) where X and Y denote the x- and the y-coordinates of the point. Each coordinate should be rounded up to the 2nd digit after the decimal point. If there are multiple such points, print the point whose x-coordinate is larger than the other.

INPUT | OUTPUT 
--- | ---
1 1 <br> 2 3 <br> 3 1 | (2.00,3.00)
3 0 <br> 0 3 <br> 2.5 2.5 | (2.50,2.50)