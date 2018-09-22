## name.py

Assume that we can name a decimal digit. For example, the following naming is possible:
```
tiger = 0, rabbit = 1, old = 2, wild = 3, east = 4, 
happy = 5, sun = 6, moon = 7, dog = 8, and cat = 9.
```
With this naming, we can evaluate a name consists of the above words. For example ¡°wild old tiger¡± corresponds to 320.

Write a program which evaluates the numeric value of a name given the names of decimal digit. Your program should print  where  is the value of the name. For example, if the name is ¡°wild old tiger,¡± your program should print 102400.

In the first line of input file, the names of digits from 0 to 9 are given separated by a space. The second line contains the name. Your program should print the square of the value of the name. 

INPUT | OUTPUT 
--- | ---
tiger rabbit old wild east happy sun moon dog cat <br> wild old tiger         | 102400
W H A T S O N Y U R <br> S O H O T          | 2038793409