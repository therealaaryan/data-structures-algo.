We will solve this question by using the approach of a cartesian plane:

We will draw position in y axis and time in x axis. The slope will become the speed. If two lines (each line indicating a car) intersects, it means that that'll become a fleet. Once it becomes the fleet, the faster car will slow down to match the slower car's speed. We will create position speed pair and maintain a stack. We will sort the positions to see the realtime positions on the road initially. Then, iterating reverse order (because faster car will cross the car that's in the front and slow down, thus making it easier to iterate), we will append the time (target - pos/speed) in the stack and if the second top element's time to reach target is less than that of the top in the stack, it means that the former is faster than the latter and we'll pop the top from the stack, beacuse it'll become same as the second top element. Finally, return the length of the stack.

  ![image](https://github.com/therealaaryan/data-structures-algo./assets/51379599/b201bf1f-8985-4b63-b020-2bf0d2441e9c)
  ![image](https://github.com/therealaaryan/data-structures-algo./assets/51379599/02c19c4c-fe26-4de0-898d-44760980ced5)

​
