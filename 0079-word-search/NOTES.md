We'll create a nested function that will take current index in the word, the row and the column.

Base case(s):
1) If the index has crossed the word, return True
2) If the row or column is out of bounds or if the letter in the cell isn't equal to the letter at current index or if the row and column pair are in path set, return False

Operation:-
Add the row and column pair to the path subset, showing that the current cell is being visited.

Recursion:-
Call recursion on r + 1, c; r - 1, c; r, c + 1; r, c - 1 while i + 1 in all of them

Operation:-
Remove the row and column pair from the path set.

FInally, traverse through every cell in the main function and call the nested function.​
