## score.py

Professor Woo teaching a programming course adopted a funny scoring scheme weighting more scores in a consecutive correct answers.

For seven problems, two students A and B got the following result:
```
	A = OOOOXXX
	B = OXOXOXO
```
where O (the alphabet O, not Zero) denotes the correct answer and X, the incorrect. Let¡¯s call this kind of string as an ¡°evaluation string.¡± In a normal scoring scheme both students have the same point 4. 

However, Professor Woo devised the following scoring scheme:
	Score[i] = Score[i-1] + 1 
where i denotes the problem number starting from 1 and Score[0] = 0. In this scheme, the list of scores of the above students can be calculated as following:
```
	Score(A) = [1, 2, 3, 4, 0, 0, 0]
	Score(B) = [1, 0, 1, 0, 1, 0, 1]
```
and the total scores of A and B are 10 and 4 respectively. 

Write a program calculating the total score according to Woo¡¯s scheme.

Input file contains a single line containing the evaluation string which consists of only O and X. The length of the evaluation string is greater than 0 and less than 100.

INPUT | OUTPUT 
--- | ---
OXOXOXO         | 4
OOOOXXX          | 10
OOOOXXXOOO    | 16
XOOXXXOOO      | 9