## addnames.py

Assume that we can name a decimal digit. For example, the following naming is possible:
```
tiger = 0, rabbit = 1, old = 2, wild = 3, east = 4, 
happy = 5, sun = 6, moon = 7, dog = 8, and cat = 9
```
With this naming, the value of the name `old rabbit` is 21 and `wild dog`, 38.

We can also define the addition of names, which consist of the words corresponding to digits, as the addition of the corresponding numeric values of the names. 

Write a program which adds two strings according to the naming of digits. For example, adding ¡°old rabbit¡± and ¡°wild dog¡± makes ¡°happy cat¡± since 21 + 38 = 59.

In the first line of input file, the names of digits from 0 to 9 are given separated by a space. The second and the third line contains name strings to add respectively. Your program should print the result of the addition as a string. 

INPUT | OUTPUT 
--- | ---
tiger rabbit old wild east happy sun moon dog cat <br> old rabbit  <br> wild dog| happy cat
W H A T S O N Y U R <br> S O <br>  H O T          | H R U