## josephus.py

Josephus problem is named after Flavius Josephus, a Jewish historian living in 1st century. Think of N persons in a circle. The problem is to execute (kill) every 2nd person until there is onle one is left.

For example, if there is five persons are, let¡¯s name them from 1 to 5. Executing every 2nd person makes the following result:

			1, 2, 3, 4, 5
		-> 	1, 3, 4, 5
		->	1, 3, 5
		-> 	3, 5
		->	3

Hence, the 3rd person survives at the end (See Fig. 1: the slashes are the persons executed during the first turn and the backslashes are those executed in the second turn).

For another example, if there is four persons are, executing every 2nd person makes the following result:

			1, 2, 3, 4
		-> 	1, 3, 4
		-> 	1, 3
		-> 	1

Hence, the 1st person survives at the end.

Your program should print the index of last person survives given the number of persons N initially. In the input file the number of persons N is given. Your program should print the index of last person survives.

INPUT | OUTPUT 
--- | ---
4 | 1
5 | 3
7 | 7
10 | 5