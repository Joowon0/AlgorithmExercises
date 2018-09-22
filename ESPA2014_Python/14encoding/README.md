## encoding.py

Encoding is a procedure or the result of representing symbols or numbers in a certain form. For example, ASCII is a kind of encoding representing digits and alphabets in a 7-bit binary format.

Owing to Zeckendorf, a Belgian mathematician, Fibonacci numbers can be used for encoding a natural number, for he found that any positive integer is the sum of non-consecutive fibonacci numbers. The following shows some examples:
```
5 = F(5) = 5
7 = F(3) + F(5) = 2 + 5
12 = F(2) + F(4) + F(6) = 1 + 3 + 8
100 = F(4) + F(6) + F(11) = 3 + 8 + 89
```
The above representations are called Zeckendorf representations. Beware that F(4) + F(6) + F(9) + F(10) is not a Zeckendorf representation even though 100 = 3 + 8 + 34 + 55 because 34 and 55 are the consecutive Fibonacci numbers.

Based on this finding, we can encode any positive integer into a binary number, 1 for including the corresponding fibonacci number into the sum and 0 for excluding. For example, assuming the encoding function E, the above numbers can be represented as the following:
```
E(5) = 0001
E(7) = 0101
E(12) = 10101
E(100) = 0010100001
```
Note that the binary digits from the left corresponds the inclusion of F(2), F(3), F(4), ¡¦ etc.; it starts from F(2) since F(2) = 1.

Write a program to print the binary encoding according to Zeckendorf. The encoding procedure can be performed in a greedy manner. To encode a positive integer N, find the biggest fibonacci number M less than or equal to N. If N ? M is not zero, repeat this procedure for N ? M. 

Your program should print the binary encoding according to Zeckendorf for given positive integer N. The input file contains N. Your program should print the binary encoding of N.

INPUT | OUTPUT 
--- | ---
4 | 101
5 | 0001
7 | 0101
12 | 10101
100 |  0010100001