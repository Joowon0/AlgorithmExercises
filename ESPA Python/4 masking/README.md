## masking.py
Masking is a special technique to hide some part of your data. This technique is typically used in printing passwords

In this homework, you¡¯d like to mask numerals only in a string. For example if you have a string:
```
"I have $20 but it is too short to buy 14 pencils."
```
then masking numerals by * shall be:
```
"I have $** but it is too short to buy ** pencils."
```

Write a program masking the numerals (numeric characters) by *. Specifically, your program should read an input line from the input file and print the result of masking the numeric characters by *.

Assume the names of the input and the output files are ¡°masking.inp¡± and ¡°masking.out¡± respectively. Your source file should be named as ¡°masking.py¡± with ¡°.py¡± is the extension.

In the input file, a single line of character string is given.

Your program should write the masking result of the input line to the output file as a single line. 

HINT: You may use the string method str.isdigit() to determine whether the character string str contains only digits.

INPUT masking.inp     | OUTPUT masking.out    
--- | ---
I have only $2.00.         | I have only $*.**.
10 is less than 123.       | ** is less than ***.