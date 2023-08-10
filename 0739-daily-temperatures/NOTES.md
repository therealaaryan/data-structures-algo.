Maintain a monotonic stack where keep adding temperatures in decreasing order and pop while top of the stack temp is less than the incoming temp. Append the difference of the indices in ans list which is initialized by all 0s


To recognize when a similar approach involving a monotonic stack could be used, look for the following characteristics in the problem:
1)Sequential Data: Problems involving sequences of data, such as temperatures, heights, prices, etc., where you need to find relationships between consecutive elements.
2)Finding Next Greater/Smaller: Situations where you need to find the next greater or next smaller element in a sequence.
3)Efficient Search: Problems where finding the next greater/smaller element in a sequence can be done more efficiently than checking all elements.
4)Stack Usage: Problems where you can use a stack to track indices or elements with certain properties and pop them off as needed.
5)Updating State: Problems where you need to update the state based on a specific condition and efficiently calculate a property.
6)Loop vs. If Statement: Use a while loop when you need to repeatedly check and process elements until a condition is no longer met. Use an if statement when you only need to check a condition once for each element.
​
