## wfamily.py
Two words are called in a same family if they are composed of the same set, actually multi-set, of characters. For example, ¡°lots¡± and ¡°lost¡± are in the same family but ¡°lost¡± and ¡°host¡± are not. As another example, ¡°mood¡± and ¡°doom¡± are in the same family.

Write a program determining two words are given in the same family.

Assume the names of the input and the output files are ¡°wfamily.inp¡± and ¡°wfamily.out¡± respectively.

In the input file, two words are given in separate lines. Each word consists of small letters only. Your program should determine they are in the same family. Print ¡°YES¡± if they are; print ¡°NO¡± otherwise.

INPUT wfamily.inp     | OUTPUT wfamily.out    
--- | ---
lots <br> lost         | YES
boys <br> girl         | NO
doom <br> mood     | YES