We'll use BFS (for loop method) to solve this. We'll do this because at a time, all the rotten oranges will rot other oranges whereas in dfs, only one rotten orange will branch out to rot other oranges.

We'll keep a fresh orange count and iterate through the grid to append to that count. While iterating, all the rotten oranges will be added to a queue to intitalize it. Then, for length of queue (and after every length iteration, append time by 1), we'll use BFS to branch out in all directions and before adding to the queue, we'll change the new r,c coordinates to rotten and then add it, while also reducing fresh orange count by 1.

In the end, if teh fresh orange count = 0, return the time else return -1.​
