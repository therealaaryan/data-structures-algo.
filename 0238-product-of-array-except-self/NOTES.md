One way to do it is to maintain two lists, prefix and postfix, that will maintain the product of all elements before the current indice in nums and same for postfix. We can then multiply them for each element's position.
To shorten the memory usage, we can combine prefix and postfix into the ans list. We will initialise prefix to 1 and append it to ans lsit and keep multiplying prefix with the corressponding index in nums to keep a track of prefix. Do the same for postfix. Return ans.


To recognize which problems might have a similar approach, look for the following patterns:
1)Problems that involve calculating a product or sum of elements for each index, considering elements on both sides of the current index.
2)Problems where you can divide the task into two parts (prefix and postfix) and then combine them to get the final result.
3)Problems where you can preprocess or cache certain information about the elements that can help you efficiently solve queries related to subarrays or individual elements.
