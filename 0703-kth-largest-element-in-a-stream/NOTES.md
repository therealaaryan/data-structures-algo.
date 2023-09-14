​Use a heap and while initializing it, heappop from the heap until k elements are remaining (heappop removes smallest element). When adding, do it using heappush and then if length of heap is greater than k, use heappop.

Knowing when to use heaps and what hints to look for in problem statements can help you recognize when this data structure is applicable. Here are some scenarios and hints to consider:

1)Finding the kth Smallest or Largest Element: If the problem involves finding the kth smallest or largest element in a collection, a heap-based approach is often suitable. In your example, the problem is to find the kth largest element in a stream.

2)Priority Queue Operations: Heaps can be thought of as a specialized form of a priority queue. If the problem requires priority queue operations like inserting elements with priorities and extracting elements with the highest or lowest priorities, a heap is a good choice. Look for keywords like "priority," "highest priority," "lowest priority," etc.

3)Top K Elements: When you need to find the top k elements (smallest or largest) from a collection, heaps are efficient. For example, finding the k largest elements in an array or stream.

4)Efficiently Maintaining Sorted Order: Heaps are useful when you need to maintain a sorted order of elements efficiently as you insert and remove elements. This is often required in problems where you need to process data in a streaming fashion.

5)Dijkstra's Algorithm and Shortest Path Problems: Heaps are used in graph algorithms like Dijkstra's algorithm to find the shortest path. If the problem involves finding the shortest path, consider using a heap.

6)Merge K Sorted Lists: When merging k sorted lists into a single sorted list, heaps can be helpful to efficiently find the smallest element among all lists.

7)Sliding Window Problems: In problems where you maintain a sliding window over a collection and need to efficiently add and remove elements from the window, heaps can be used to keep track of the maximum or minimum element in the current window.

8)Median Maintenance: Heaps can be used to efficiently maintain the median of a collection of elements as elements are inserted or removed.
