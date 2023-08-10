We will use a double ended decreasing monotonic queue to solve this. The basic concept is that the queue will contain indices of elements (for window purposes) and the indices will be added in such a way that the elements associated with the indices are in a decreasing order. Hence for a window, the index at front of the queue will represent the maximum element in the window. When we traverse nums, if the element at right pointer happens to be greater than the one at the back of the queue, we'll pop that element and this will keep going on till the element at the back is greater than the incoming element. Only then we shall append to the queue. This helps maintain the decreasing order of the queue. If left pointer is greater than the index at front of the queue, it means that tha telement is out of teh window hence remove it from teh queue.


To recognize when a similar approach using a monotonic queue may be used, look for the following characteristics in the problem:
1)Sliding Window: Problems that involve finding the maximum (or minimum) element in each sliding window or a range of elements.
2)Efficient Tracking: Situations where you need to efficiently update and maintain certain characteristics or properties of the current window or subarray.
3)Monotonic Property: Problems that can be optimized by using a monotonic data structure (e.g., monotonic queue, monotonic stack) to keep elements in a certain order (increasing or decreasing).
4)Deque Operations: Problems where you need to perform deque operations (popping from both ends, appending to both ends) to efficiently update the data structure.
​
