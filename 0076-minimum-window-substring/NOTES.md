Maintain two hashmaps, ds and dt. dt will map the frequency of its elements and ds will only have the elements. Iterate using sliding window and if element added in the window is present as a key in ds, append its occurrence in ds and if the frequency of that element matches of that in dt, append 1 to a count variable. While count is equal to length of dt, keep shifting l and removing its occurence if present in ds and also check if window length is less than previously encountered, store the window in ans.


To recognize when a similar approach with two pointers and a count variable could be used, look for the following characteristics in the problem:
1)Sliding Window: Problems where you need to consider a window or substring of variable length within a larger string or array.
2)Checking Conditions: Problems where you need to check for certain conditions in the window and dynamically adjust the window based on those conditions.
3)Track of Required Elements: Problems that require keeping track of the presence or frequency of certain elements or characters.
4)Optimization using Pointers: Situations where using two pointers to slide the window efficiently can lead to a more optimized solution.
​
