There are two methods to solve this:-
1) We will basically use the idea of traversing every element of the array and see how much water can be filled in this element. To do that, we'll calculate the highest wall on both, left and right sides, of the element and find the minimum of the two (for the bottleneck). Then, for every element, we'll subtract the height of the element wall from the minimum we found. If the asnwer is negative, it means that the bottom is greater than the bottleneck, hence we can't store water there. Create a list for maximum elements for both left and right sides.

2) Instead of creating two lists, we can use two pointer approach to reduce space complexity. We will set l and r at two extreme ends of the given list and shift the one that is less compared to other. That will become the bottleneck and then apply the same formula as above.



To recognize problems where similar approaches can be used, look for the following characteristics:
1)Bottleneck Consideration: Problems where the amount of trapped or collected something (water, rain, etc.) depends on the minimum or maximum of certain values from both ends or surrounding elements.
2)Two-Pointer Technique: Problems that involve traversing elements from both ends and making decisions based on the minimum or maximum values encountered during traversal.
3)Sliding Window-Like Behavior: Problems where you can optimize calculations by sliding a window or two pointers from both ends while keeping track of certain characteristics.
4)Observing Local and Global Optima: Problems where considering local and global optima simultaneously is essential for arriving at the correct answer.
​
