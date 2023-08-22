​The issue with this problem is there are 2 edge cases we need to consider:

1) for eg if it is 17 + 8, then we'll have to keep going on till both the linked lists are iterated.
2) for eg if it is 8 + 7, even though both the lists are over in first iteration, there is a carry of 1 still remaining.

We will create a dummy list and iterate till there is l1 or l2 or carry. If l1 or l2 aren't there, set their value as 0 and keep going.
