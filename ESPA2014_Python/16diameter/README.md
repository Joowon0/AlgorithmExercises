## diameter.py

Once the distance of two points  and  is defined as d(, ), the diameter of a set of points P can be defined as follows:
	D(P) = max { d(pi, pj) | pi, pj  P }

As you know, the distance of two points  and  in a 2-dimensional plane is defined as follows:
	d(p1, pj) = 

You would like to write a program calculating the diameter of a set of points in two dimensional space. For this, define and use the class Point representing the points in the two dimensional space.

If you have two Point objects, p1 and p2, the distance d between these points may be calculated as follows: d = p1.dist(p2);

For example, if the following five points are given as input:     and , the diameter is calculated as 5.0 as depicted in the figure.

The input file contains the coordinates of points. The x- and y-coordinates of a point is given in a single input line, separated by a space. The coordinates are given as floating-point numbers. Assume that the number of points is at least 2, i.e. |P| > 1. Your program should print the diameter of a set of points to the output file, up to the second digit after the decimal point.

INPUT | OUTPUT 
--- | ---
1.0 1.0 <br> 2.1 0.5 <br> 3.4 2.9 <br> 2.5 3.1 <br> 5.0 4.0 | 5.00
1.3 0.2 <br> 0.3 1.2 |  1.41