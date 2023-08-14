There'll be two cases:
1) If the array is rotated, then the left pointer element will be greater than right pointer element. Set the mid and if mid is greater than right, shift left to mid + 1, else right to mid - 1.
2) If the array isn't rotated, ans will be the first element of the array.
​
