We'll basically maintain a hashmap (use collections.defaultdict to avoid errors popping up when the dict is empty) for rows, columns and 3x3 squares where the keys will be the row number, column number and square grid identification(it'll be a tuple of r//3 and c//3) and the values will be a set or an array. While iterating through the soduku, we'll check if the current element exists in the keys of any of the 3 hashmaps. Return False if it does. Finally, append to all 3 hashmaps the element we encountered. Default return True.


When facing problems where you need to keep track of unique elements or their occurrences within specific regions or groups, using hashmaps (or sets) is a common approach. Here are some common patterns where this technique can be applied:
1)Group-Based Validation: Problems where you need to validate the uniqueness of elements within specific groups, such as rows, columns, grids, or subarrays.
2)Frequency Counting: Problems where you need to count the occurrences of elements in an array, string, or matrix, and identify duplicates or unique elements.
3)Checking Constraints: Problems where you need to check whether a given configuration or arrangement satisfies certain constraints, and hashmaps (or sets) can help you efficiently enforce and validate those constraints.
​
